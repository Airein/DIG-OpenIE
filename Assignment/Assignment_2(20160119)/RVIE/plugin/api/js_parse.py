
import json
import os
from ... import __root_dir__, __raw_outputs__

class JSHelper():
    # root_dir = os.path.abspath(__file__ + "/../../../")

    def __init__(self):
        pass

    def es_name_extractor(self, filename):
        names = []
        valid_name = ['a', 'i']
        json_file = open(filename, 'rU')
        data = json.load(json_file) 
        buckets = data['aggregations']['name']['buckets']
        output = open(__root_dir__ + '/' + __raw_outputs__ + 'names.raw', 'wb')
        for bucket in buckets:
            name = bucket['key']
            if name in valid_name or len(name) == 1:
                continue
            names.append(name)
            output.write(str(name) + '\n')
        output.close()
        return names


    def es_desc_extractor(self, filename):
        # print 'aa '+filename
        file_name = filename.split('/')[-1].split('.')[0]
        # print file_name

        json_file = open(filename, 'rU')
        data = json.load(json_file) 
        hits = data['hits']['hits']
        output = open(__root_dir__ + '/' + __raw_outputs__ + 'sentences/' + file_name +'.raw', 'wb')
        for hit in hits:
            try:
                # may not have description
                desc = hit['_source']['description']
            except Exception as e: 
                """
                print('Not description filed:')
                print(str(hit) + '\n')
                """
            desc_info = desc[0].encode('utf-8').strip()
            output.write(desc_info + '.\n')
        output.close()

        


