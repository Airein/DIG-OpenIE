"""
Author: Lingzhe Teng
Date:   Jan. 21, 2016

"""

"""
Description:

required: 
pip install --user pycurl

"""
import pycurl
from StringIO import StringIO

# class Curl_Helper:
HOST_NAME = 'https://esc.memexproxy.com/dig-ht-california-ads-trial01-optimized/adultservice/_search'
HTTP_HEADER = ['Cache-Control: no-cache',
                'Authorization: Basic ZGFycGFtZW1leDpkYXJwYW1lbWV4',
                'Postman-Token: 6fdf344b-1901-12d1-42af-865fc92a1103']
OUTPUT_FOLDER = '../data/json/'



def fetch2buf(host=HOST_NAME, query='', buf=StringIO()):
    # buf = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, host)
    c.setopt(c.POSTFIELDS, query)
    c.setopt(c.VERBOSE, True)
    c.setopt(c.WRITEDATA, buf)
    c.setopt(pycurl.HTTPHEADER, HTTP_HEADER)
    c.perform()
    c.close()

    # body = buf.getvalue()
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    # print(body)

def fetch2file(host=HOST_NAME, query='', filename='output'):
    with open(OUTPUT_FOLDER+filename, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, host)
        c.setopt(c.POSTFIELDS, query)
        c.setopt(c.VERBOSE, True)
        # c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.WRITEDATA, f)
        c.setopt(pycurl.HTTPHEADER, HTTP_HEADER)
        c.perform()
        c.close()


if __name__ == '__main__':
    
    query = '{"aggs": {"name": {"terms": {"field": "name","size": 500}}},"size": 0}'

    # ch = Curl_Helper()
    fetch2file(HOST_NAME, query, "aaa")

    """
    # Test, fetch to buffer
    buffer = StringIO()
    ch.fetch2buf(buffer, query)
    body = buffer.getvalue()
    print(body)
    """
