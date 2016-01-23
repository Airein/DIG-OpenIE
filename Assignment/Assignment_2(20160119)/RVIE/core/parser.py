from os import listdir
from os.path import isfile, join

from ..plugin import api
from .. import __json_outputs__, __raw_outputs__, __root_dir__

class JSparser(object):
    def __init__(self):
        self.js_parser = api.JSHelper()

    def parse(self):
        pass
        

    def parseName(self):
        path = __root_dir__ + __json_outputs__
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
        names = []
        for jsf in onlyfiles:
            names.extend(self.js_parser.es_name_extractor(path + jsf))
        return names


    def parseSentence(self):
        # self.js_parser.es_desc_extractor()
        # print __root_dir__
        path = __root_dir__ + __json_outputs__ + 'sentences/'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
        # print path
        # print onlyfiles
        
        for jsf in onlyfiles:
            # print path + jsf
            self.js_parser.es_desc_extractor(path + jsf) 
        

