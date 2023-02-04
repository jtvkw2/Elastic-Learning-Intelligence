## Doing
- [ ] Fix Ingestion Script for new mapping schema

## Done
- [x] Moved from Streamlit to Flask
- [x] Added Base Templates
- [x] Completed Neo4j Ingestion Script
- [x] Create Search Field Template  
- [x] Use Elastic to create elastic nodes
- [x] Finish Data Ingestion Class
- [x] Dockerize flask app
- [x] Add Elastic to Docker build


## Backlog

- [ ] Add autocomplete using existing imported data
- [ ] Rank Adjacent data in details with recomendation engine
- [ ] Add Flask Login
  - [ ] Create seperate views based on login (i.e. Admin Panel)
  - [ ] Maybe search history and saved data?
    - [ ] Initialize database in docker volumes
- [ ] Create data ingestion API
- [ ] Add dropdown for initial search filtering on search page
- [ ] Finish settings page for creation of mapping files from Node class creation
  - [ ] Modularize in a way that more data formats and graph dbs can be added later
  - [ ] Need to seperate out data sources
- [ ] Create custom Name Entity Recognition model with custom glossary
  - [ ] This needs to find node classes first for better filtering
