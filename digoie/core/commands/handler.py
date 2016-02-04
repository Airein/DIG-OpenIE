
from digoie.core.http.stream.base import stream
from digoie.core.extractor.reverb import extract
from digoie.core.ml.dataset.base import generate_dataset
from digoie.core.ml.classifier.base import generate_classifier
from digoie.core.ml.classifier.predict import predict

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
        mla = 'decision_tree'
        if opt['--mla']:
            mla = opt['--mla']

        feature_names, X_train, X_test, y_train, y_test = generate_dataset()
        clf = generate_classifier(X_train, X_test, y_train, y_test, mla)
    elif opt['predict']:
        print 'predict handler'
        test_only = 'My name is Jassica.'
        predict(test_only)
    else:
        print(opt)