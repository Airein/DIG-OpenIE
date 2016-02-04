import os
import json
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, ES_RAW_EXT, REVERB_INPUT_EXT


def parse_name(raw):
    print 'parse names from json...'
    # input_filename = 'names' + ES_RAW_EXT
    # input_path = os.path.join(__elastic_search_dir__, input_filename)
    # output_filename = 'names' + REVERB_INPUT_EXT
    # output_path = os.path.join(__reverb_input_dir__, output_filename)

    # input_file = open(input_path, 'rU')
    # output_file = open(output_path, 'wb')
    
    names = []
    invalid_name = ['as', 'if']
    # raw = json.load(input_file)
    raw = json.loads(raw)
    
    # detect structure
    buckets = raw['aggregations']['name']['buckets']
    # output = open(__root_dir__ + '/' + __raw_outputs__ + 'names.raw', 'wb')
    for bucket in buckets:
        name = bucket['key']
        if name in invalid_name or len(name) == 1:
            continue
        names.append(name)
        # output.write(str(name) + '\n')
    # input_file.close()
    # output_file.close()
    return names

    # onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
    # names = []
    # for jsf in onlyfiles:
    #     names.extend(self.js_parser.es_name_extractor(path + jsf))
    # return names


def parse_sentence(raw):
    raw = json.loads(raw)
    sentences = []
    hits = raw['hits']['hits']
    for hit in hits:
        try:
            # may not have description
            desc = hit['_source']['description']
        except Exception as e: 
            pass
        
        desc_info = desc[0].encode('utf-8').strip()
        sentences.append(desc_info + '.')
    return sentences

    

    """
    path = __root_dir__ + __json_outputs__ + 'sentences/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
    
    for jsf in onlyfiles:
        print 'parse sentences for ' + path + jsf
        self.js_parser.es_desc_extractor(path + jsf) 
    """

        