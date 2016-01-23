

import pycurl
# import os
from StringIO import StringIO

from ... import __root_dir__

HTTP_HEADER = ['Cache-Control: no-cache',
                'Authorization: Basic ZGFycGFtZW1leDpkYXJwYW1lbWV4',
                'Postman-Token: 6fdf344b-1901-12d1-42af-865fc92a1103']

class CURLHelper():
    def __init__(self):
        self.curl_conn = pycurl.Curl()

        # show or hide verbose for curl
        self.curl_conn.setopt(self.curl_conn.VERBOSE, False)
        self.curl_conn.setopt(pycurl.HTTPHEADER, HTTP_HEADER)
        # self.curl_conn.setopt(pycurl.WRITEFUNCTION, lambda x: None)

        
    def fetch2buf(self, url, query, buf):
        c = self.curl_conn
        # buf = StringIO()
        c.setopt(c.URL, url)
        c.setopt(c.POSTFIELDS, query)
        c.setopt(c.WRITEDATA, buf)
        c.perform()
        # c.close()

    def fetch2file(self, url, query, filename):
        # print "------------------------------------"
        c = self.curl_conn
        # root_dir = os.path.abspath(__file__ + "/../../../")
        # print "------------------------------------"

        with open(__root_dir__ + '/' + filename, 'wb') as f:
            c.setopt(c.URL, url)
            c.setopt(c.POSTFIELDS, query)
            c.setopt(c.WRITEDATA, f)
            c.perform()
            # c.close()




if __name__ == '__main__':
    c = CURLHelper("s")
    # c.foo()