"""
Author: Lingzhe Teng
Date:   Jan. 21, 2016

"""


import sys
import os
import subprocess
import constants


from datafetcher import curl_fetcher
from extractor import json_extractor
from reverb import rv_helper
from StringIO import StringIO



def load_data():
    # query = '{"aggs": {"name": {"terms": {"field": "name","size": 500}}},"size": 0}'
    host = 'https://esc.memexproxy.com/dig-ht-california-ads-trial01-optimized/webpage/_search'
    query = '{ "query": {   "query_string": {     "query": "tiffany"   } }, "size": 200, "_source": {   "includes": [     "description"   ] }}'

    curl_fetcher.fetch2file(host, query, constants.DT_JSON_FOLDER+"try.json")
    # buf = StringIO()
    # curl_fetcher.fetch2buf(host, query, buf)
    # inventory = json.loads(buf.getvalue())
    # print json.dumps(inventory)

def parse_data():
    json_extractor.es_desc_extractor(constants.DT_JSON_FOLDER+'try.json')

    

def lauch_reverb():
    f = open(constants.DT_REVERB_FOLDER+"reverb.output","a")
    argsArray = ['java', '-Xmx512m', '-jar', 'reverb/reverb-core-1.4.3-SNAPSHOT-jar-with-dependencies.jar', DT_RAW_FOLDER+'test.raw']
    subprocess.call(argsArray, stdout=f)

if __name__ == '__main__':
    # fetch data by elastic search
    # load_data()

    # parse json data
    # parse_data()
    

    # run reverb
    # lauch_reverb()

    # load and preprocess reverb output
    rv_helper.load_rv_data(constants.DT_REVERB_FOLDER+"reverb.output")






