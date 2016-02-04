import pycurl

HTTP_HEADER = ['Cache-Control: no-cache',
                'Authorization: Basic ZGFycGFtZW1leDpkYXJwYW1lbWV4',
                'Postman-Token: 6fdf344b-1901-12d1-42af-865fc92a1103']



class HTTPClient(object):
    def __init__(self, enable_verbose=False):
        self.curl_conn = pycurl.Curl()

        # show or hide verbose for curl
        self.curl_conn.setopt(self.curl_conn.VERBOSE, enable_verbose)
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
    

    def fetch2file(self, url, query, path):
        c = self.curl_conn
        with open(path, 'wb') as f:
            c.setopt(c.URL, url)
            c.setopt(c.POSTFIELDS, query)
            c.setopt(c.WRITEDATA, f)
            c.perform()
            # c.close()
