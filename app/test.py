import json
from utils.ingest import Insert

with open("config/mappings.json") as m:
    config_mappings = json.loads(m.read())
    
ingest = Insert(config_mappings=config_mappings)
records = ingest.from_csv("data/people.csv", "person")
print(records)