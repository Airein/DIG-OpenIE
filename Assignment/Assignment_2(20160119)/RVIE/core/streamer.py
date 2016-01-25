
from ..plugin import api
from .. import __json_outputs__


NAMESTREAM_URL = 'https://esc.memexproxy.com/dig-ht-california-ads-trial01-optimized/adultservice/_search'
SENTENCESTREAM_URL = 'https://esc.memexproxy.com/dig-ht-california-ads-trial01-optimized/webpage/_search'


class ESstreamer(object):
    def __init__(self):
        self.curl_request = api.CURLHelper()

    def streams(self):
        # Names Stream
        self.fetch_names()
        
        # Sentences with Name Stream
        self.fetch_sentences()

    def fetch_names(self):
        filename = 'names.json'
        print 'fetch names... output at: ' + __json_outputs__ + filename
        query = api.names_query()
        self.curl_request.fetch2file(NAMESTREAM_URL, query, __json_outputs__ + filename)

    def fetch_sentences(self, name=None):
        filename = name + '.json'
        print 'fetch sentences for name ' + name +'... output at: ' + __json_outputs__ + filename
        query = api.namesentences_query(name)
        self.curl_request.fetch2file(SENTENCESTREAM_URL, query, __json_outputs__ + 'sentences/' + filename)





if __name__ == '__main__':
    c = api.CURLHelper()
    # c.foo()
    # api.sss()
