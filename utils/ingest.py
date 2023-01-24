# External Imports
from datetime import date
import pandas as pd
from neo4j import GraphDatabase
import sys
import json

class Insert:
    def __init__(self, config, config_mappings):
        self.db = GraphDatabase.driver(config['Neo4j']['DATABASE_URL'])
        self.records = None
        self.mapped_records = None
        self.config_mappings = config_mappings
        
    def is_valid_type(self, input_type):
        if input_type in self.config_mappings:
            return True
        else:
            return False
    
    def get_node_definitions(self, node_type):
        if node_type in self.config_mappings:
            return self.config_mappings[node_type]
    
    def from_csv(self, input_csv, input_type):
        assert self.is_valid_type(input_type)
        df = pd.read_csv(input_csv)
        self.records = df.to_dict(orient='records')
        self.mapped_records = self.map_to_json(self.records[0], input_type, self.config_mappings)
        return self.mapped_records
        
    def map_to_json(self, input_data, data_type, neo4j_mappings):
        curr_data = neo4j_mappings[data_type]
        result_json = {}
        for node, values in curr_data.items():
            curr_node = {}
            for node_name, data_name in values.items():
                curr_value = input_data[data_name]
                if isinstance(curr_value, str):
                    curr_value = curr_value.lower()
                curr_node[node_name] = curr_value
            result_json[node] = curr_node
        return result_json
    
    def create_node(self, values):
        query = f"""
        CREATE (a: {values['node_type']} {values['node_properties']})
        RETURN a.id
        """
        result = self.db.run(query)
        for record in result:
            return record['a.id']
        
    def create_relationship(self, values):
        query = """
        MATCH (a) where a.id = $n1
        MATCH (b) where b.id = $n2
        with a, b
        MERGE (a)-[:$relationship]->(b)
        """
        self.db.run(query, values)
        
    def insert_data(self, es):
        for record in self.mapped_records:
            node_id = self.create_node(record['node'])
            record['node']['id'] = node_id
            for relationship in record['relationships']:
                relationship['n1'] = node_id
                self.create_relationship(relationship)
         # Insert node_id and searchable terms into Elasticsearch
            elasticsearch_data = {
                'node_type': record['node']['node_type'],
                'node_properties': record['node']['node_properties'],
                'relationships': {},
                'tags': record['tags']
            }
            for relationship in record['relationships']:
                elasticsearch_data['relationships'][relationship['type']] = relationship['n2']
            es.index(index=f'{record["node"]["node_type"].lower()}_index', id=node_id, body=elasticsearch_data)