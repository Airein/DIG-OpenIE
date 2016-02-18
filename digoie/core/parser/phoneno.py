
import json

def parse_sentence(raw):
    raw = json.load(raw)
    sentences = []
    hits = raw['hits']['hits']
    for hit in hits:
        try:
            # may not have description
            desc = hit['_source']['crawl_data']['content']
        except Exception as e: 
            pass
        
        desc_info = desc.encode('utf-8').strip()
        sentences.append(desc_info + '.')
    return sentences