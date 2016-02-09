
import os
from digoie.conf.storage import __reverb_input_dir__, __elastic_search_dir__, REVERB_INPUT_EXT
from digoie.core.http.stream.httpclient import HTTPClient
from digoie.core.http.elasticsearch.query import *
from digoie.core.http.elasticsearch.url import NAMESTREAM_URL, SENTENCESTREAM_URL
from digoie.core.parser.elasticsearch import *
from StringIO import StringIO
from digoie.utils.symbols import do_newline_symbol


def stream_names():
    names = fetch_names()
    for name in names:
        filename = name + REVERB_INPUT_EXT
        path = os.path.join(__reverb_input_dir__, filename)
        sentence_file = open(path, 'wb')
        sentence_file.writelines(line + do_newline_symbol() for line in fetch_sentences(name))
        sentence_file.close()


def fetch_names():
    query = es_names_query()
    buf = StringIO()
    HTTPClient().fetch2buf(NAMESTREAM_URL, query, buf)
    names_json = buf.getvalue()
    names = [str(name) for name in parse_name(names_json)]

    # write names
    path = os.path.join(__elastic_search_dir__, 'names')
    sentence_file = open(path, 'wb')
    sentence_file.writelines(line + do_newline_symbol() for line in names)
    sentence_file.close()

    return names

def fetch_sentences(name):
    print 'fetch sentences for name ' + name
    query = es_sentences_query(name)
    buf = StringIO()
    HTTPClient().fetch2buf(SENTENCESTREAM_URL, query, buf)
    sentences_json =  buf.getvalue()
    return parse_sentence(sentences_json)