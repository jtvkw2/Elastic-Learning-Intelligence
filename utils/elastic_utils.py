def check_and_create_index(es, folder_mappings):
    """
    Takes defined folder mappings from config file and creates an index if they don't already exist
    
    Args:
        es: Elasticsearch client instance.
        folder_mappings: An array of folder locations and their associated es mapping
    """
    pass
    # for elem in folder_mappings:
    #     index = elem[0]
    #     mapping = elem[1]
    #     if not es.indices.exists(index):
    #         es.indices.create(index=index, body=mapping, ignore=400)


def index_search(es, index: str, keywords: str, filters: str,
                 from_i: int, size: int) -> dict:
    """
    Args:
        es: Elasticsearch client instance.
        index: Name of the index we are going to use.
        keywords: Search keywords.
        filters: Tag name to filter medium stories.
        from_i: Start index of the results for pagination.
        size: Number of results returned in each search.
    """
    # search query
    body = {
        'query': {
            'bool': {
                'must': [
                    {
                        'query_string': {
                            'query': keywords,
                            'fields': ['content'],
                            'default_operator': 'AND',
                        }
                    }
                ],
            }
        },
        'highlight': {
            'pre_tags': ['<b>'],
            'post_tags': ['</b>'],
            'fields': {'content': {}}
        },
        'from': from_i,
        'size': size,
        'aggs': {
            'tags': {
                'terms': {'field': 'tags'}
            },
            'match_count': {'value_count': {'field': '_id'}}
        }
    }
    if filters is not None:
        body['query']['bool']['filter'] = {
            'terms': {
                'tags': [filters]
            }
        }

    res = es.search(index=index, body=body)
    # sort popular tags
    sorted_tags = res['aggregations']['tags']['buckets']
    sorted_tags = sorted(
        sorted_tags,
        key=lambda t: t['doc_count'], reverse=True
    )
    res['sorted_tags'] = [t['key'] for t in sorted_tags]
    return res