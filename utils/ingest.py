# External Imports
from datetime import date
import pandas as pd
from neomodel import db
import sys
import json

# Internal Imports
sys.path.append('../')
from config import config, json_mappings, node_class_mappings

class Insert:
    def __init__(self):
        self.db = db.set_connection(config.DATABASE_URL)
        self.records = None
        self.mapped_records = None
        
    def is_valid_type(self, input_type):
        if input_type in json_mappings.neo4j_mappings:
            return True
        else:
            return False
    
    def get_node_definitions(self, node_type):
        if node_type in node_class_mappings.node_mappings:
            return node_class_mappings.node_mappings[node_type]
    
    def from_csv(self, input_csv, input_type):
        assert self.is_valid_type(input_type)
        df = pd.read_csv(input_csv)[:10]
        self.records = df.to_dict(orient='records')
        self.mapped_records = self.map_to_json(self.records[0], input_type, json_mappings.neo4j_mappings)
        return self.mapped_records
        #self._run()
        
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
    
    @staticmethod
    def _run(self):
        pass
        #node
        #create_nodes(node_info)
        
        
        
insert = Insert()
print(json.dumps(insert.from_csv("../data/CSV/complaints.csv", "C360")))