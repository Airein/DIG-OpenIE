
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
        # mla = 'decision_tree'
        min_df = 0.0001
        max_df = 0.5
        if opt['--min_df']:
            min_df = opt['--min_df']

        if opt['--max_df']:
            max_df = opt['--max_df']

    
        feature_names, X_train, X_test, y_train, y_test = generate_dataset(min_df, max_df)

        if opt['--mla']:
            mla = opt['--mla']
            clf = generate_classifier(X_train, X_test, y_train, y_test, mla)
        else:
            clf = generate_classifier(X_train, X_test, y_train, y_test)
    elif opt['predict']:
        print 'predict handler'
        test_only = 'My name is Jassica.'
        predict(test_only)
    else:
        print(opt)