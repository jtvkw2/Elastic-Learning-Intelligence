"""
Search Engine Demo

Author: Jacob Voyles
Date 12/30/2022

"""

# External Library Imports
import urllib.parse
import json
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

# Internal Imports
from utils.elastic_utils import search_elasticsearch
from utils.entitiy_recognition import EntityRecognition
from utils.neo4j_utils import get_details
from utils.ingest import Insert

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

with open("config/config.json") as c:
    config = json.loads(c.read())
    
with open("config/mappings.json") as m:
    config_mappings = json.loads(m.read())
    
es = Elasticsearch(hosts=config['Elasticsearch']['Host'])
 
@app.route('/', methods = ["GET", "POST"])
def home():
    res = []
    if request.method == "POST":
        er = EntityRecognition()
        res = er.run(request.form['search'])
        #results = search_elasticsearch("Person", "John")
    if res:
        css_height = "5"
    else:
        css_height = "20"
    return render_template('search.html', er = res, css_height = css_height)
 
@app.route('/settings', methods = ["GET", "POST"])
def settings():
    if request.method == "POST":
        key = request.form['key']
        title = request.form['title']
        value = request.form['value']
        config[key][title] = value
        with open("config/config.json", 'w') as f:
            json.dump(config, f, indent=4)
    return render_template('settings.html', config = config)

@app.route('/mappings', methods = ["GET", "POST"])
def mappings():
    return render_template('mappings.html', maps = config_mappings)

@app.route('/detail', methods = ["GET", "POST"])
def results():
    detail_id = 0
    details = get_details(detail_id)
    return render_template('result.html', details = details)

@app.route('/ingest', methods = ["GET", "POST"])
def ingest():
    ingest = Insert(config=config, config_mappings=config_mappings)
    records = ingest.from_csv("data/people.csv")
    print(records)

# main driver function
if __name__ == '__main__':
    app.run()