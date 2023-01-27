# ElasticGraph

![ElasticGraph Logo](static/images/logo-banner.png "Title")

A semantic search engine webapp built onto of a neo4j database which is indexed using ElasticSearch. Designed to connect and search large amounts of data from a simple user interface. 

## This Project is Still Under Development
Please check back later to use this tool once I have a release or help contribute to the project.

## ToDos - Need to move this to Issues
- [ ] Add Flask Login
  - [ ] Create seperate views based on login (i.e. Admin Panel)
  - [ ] Maybe search history and saved data?
    - [ ] Initialize database in docker volumes
- [ ] Dockerize app
  - [ ] Add Elastic to Docker build
  - [ ] Neo4j in Docker build
  - [ ] Make elastic and neo optional params
  - [ ] Seperate utils into package and seperate out flask
    - [ ] Insert API as part of package and use flask as http endpoint
    - [ ] Add package as seperate comonent for PyPi
- [ ] Fix Data Ingestion
- [ ] Create data ingestion API
- [ ] Add dropdown for initial search filtering on search page
- [ ] Finish settings page for creation of mapping files from Node class creation
  - [ ] Modularize in a way that more data formats and graph dbs can be added later
  - [ ] Need to seperate out data sources
- [ ] Create custom Name Entity Recognition model with custom glossary
  - [ ] This needs to find node classes first for better filtering
  - [ ] Should be able to be called from Ingestion package


## Instalation

## Configuration

## Usage

## Limitations

## Support the project

[<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="180" height="50" >](https://www.buymeacoffee.com/jtvkw2)
