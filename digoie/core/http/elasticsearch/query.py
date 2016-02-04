
def es_names_query(size=500):
    return '{"aggs": {"name": {"terms": {"field": "name","size": ' + str(size) + '}}},"size": 0}'

def es_sentences_query(name='tiffany', size=200):
    return '{ "query": {   "query_string": {     "query": "'+ name + '"   } }, "size": ' + str(size) + ', "_source": {   "includes": [     "description"   ] }}'