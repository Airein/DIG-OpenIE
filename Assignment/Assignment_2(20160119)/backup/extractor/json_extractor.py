
import json

def es_desc_extractor(filename):
    json_file = open(filename)
    data = json.load(json_file) 
    hits = data['hits']['hits']

    f = open('data/raw/'+"test.raw","a")

    for hit in hits:
        desc = hit['_source']['description']
        f.write(str(desc[0]) + '.\n')
    f.close()

