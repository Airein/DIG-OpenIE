
from digoie.core.http.stream.base import stream
from digoie.core.extractor.reverb import extract
from digoie.core.ml.dataset.base import generate_dataset
# import digoie.core.ml

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
    elif opt['classifier']:
        print 'classifier handler'
        generate_dataset()


    else:
        print(opt)