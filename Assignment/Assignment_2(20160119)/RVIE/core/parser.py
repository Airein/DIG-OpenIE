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
        print 'parse names from json... output at: ' + __raw_outputs__ + 'names.raw'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
        names = []
        for jsf in onlyfiles:
            names.extend(self.js_parser.es_name_extractor(path + jsf))
        return names


    def parseSentence(self):
        path = __root_dir__ + __json_outputs__ + 'sentences/'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[-1] == 'json']
        
        for jsf in onlyfiles:
            print 'parse sentences for ' + path + jsf
            self.js_parser.es_desc_extractor(path + jsf) 
        

