
from digoie.core.http.stream.base import stream
from digoie.core.extractor.reverb import extract
from digoie.core.ml.dataset.base import generate_dataset
from digoie.core.ml.classifier.base import *


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
        # X_train, X_test, y_train, y_test = generate_dataset()
        train()
    else:
        print(opt)