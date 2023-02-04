def search_elasticsearch(es, node_type, query_string):
    index = f"{node_type.lower()}_index"
    body = {
        "query": {
            "query_string": {
                "query": query_string
            }
        },
        "aggs": {
            "tags": {
                "terms": {
                    "field": "tags"
                }
            }
        }
    }
    results = es.search(index=index, body=body)
    return results