
from digoie.core.http.stream.base import stream
from digoie.core.extractor.reverb import *

def cmd_hander(opt):
    if opt['--interactive']:
        pass
        # MyInteractive().cmdloop()
    elif opt['stream']:
        print 'stream handler'
        stream(opt)
    elif opt['dataset']:
        print 'dataset handler'
        extract()
    else:
        print(opt)