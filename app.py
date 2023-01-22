"""
Search Engine Demo

Author: Jacob Voyles
Date 12/30/2022

"""

# External Library Imports
import urllib.parse
import json
from flask import Flask, render_template
from elasticsearch import Elasticsearch

# Interanal Imports
from config import config
from utils import elastic_utils, template
from utils.entitiy_recognition import EntityRecognition

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('search.html')
 
# main driver function
if __name__ == '__main__':
    app.run()