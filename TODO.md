## Doing
- [ ] Make Neo4j Optional
- [ ] Use Elastic to create elastic nodes
- [ ] Dockerize app
- [ ] Add Elastic to Docker build

## Done
- [x] Moved from Streamlit to Flask
- [x] Added Base Templates
- [x] Completed Neo4j Ingestion Script
- [x] Create Search Field Template  

## Backlog

- [ ] Add autocomplete using existing imported data
- [ ] Rank Adjacent data in details with recomendation engine
- [ ] Add Flask Login
  - [ ] Create seperate views based on login (i.e. Admin Panel)
  - [ ] Maybe search history and saved data?
    - [ ] Initialize database in docker volumes
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
