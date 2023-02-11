# External Imports
from datetime import date
import pandas as pd
import sys
import json

class Insert:
    def __init__(self, config_mappings):
        self.records = None
        self.mapped_records = []
        self.config_mappings = config_mappings
    
    def get_node_definitions(self, node_type):
        if node_type in self.config_mappings:
            return self.config_mappings[node_type]
    
    def from_csv(self, input_csv, input_type, es):
        df = pd.read_csv(input_csv)
        self.records = df.to_dict(orient='records')
        for record in self.records:
            self.mapped_records.append(self.map_to_json(record, input_type, self.config_mappings))
        self.insert_data(es)
        
    def map_to_json(self, input_data, data_type, config_mappings):
        curr_data = config_mappings[data_type]
        result_json = {"node": {}, "relationships" : []}
        for node, values in curr_data.items():
            if node == 'node_type':
                result_json['node']['type'] = values
            if node == 'node_id':
                result_json['node']['id'] = input_data[values]
            if node == 'node_properties':
                for node_name, data_name in values.items():
                    curr_value = input_data[data_name]
                    if isinstance(curr_value, str):
                        curr_value = curr_value.lower()
                    result_json['node'][node_name] = curr_value
            if node == 'relationships':
                for elem in values:
                    curr_rel = {
                        "node_type": elem['node_type'],
                        "relationship": elem['relationship'],
                        "id" : input_data[elem['id']],
                        "rank" : 0
                    }
                    result_json['relationships'].append(curr_rel)
            result_json['tags'] = 'tag'
        return result_json
        
    def insert_data(self, es):
        records_added = 0
        for record in self.mapped_records:
            elasticsearch_data = {
                'id': record['node']['id'],
                'node_type': record['node']['type'],
                'relationships': record['relationships'],
                'tags': record['tags'],
            }
            for key, val in record['node'].items():
                if key not in ('type', 'id', 'tags'):
                    elasticsearch_data[key] = val
            print(elasticsearch_data)
            es.index(index=f'{record["node"]["type"].lower()}_index', id=record['node']['id'], body=elasticsearch_data)
            records_added += 1
        return records_added