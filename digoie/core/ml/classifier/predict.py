
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from digoie.core.ml.dataset.model import load_model
from digoie.conf.machine_learning import MACHINE_LEARNING_ALGORITHMS, DECISION_TREE, RANDOM_FOREST, AdaBoost, Gaussian_Naive_Bayes
# from digoie.core.extractor.reverb import lauch4String
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset.vector import vectorize, load_feature_names
from digoie.core.ml.dataset.base import generate_dataset
from digoie.core.ml.classifier.base import generate_classifier
from digoie.core.extractor import reverb
from digoie.conf.storage import __predict_dir__, __pred_data_dir__, __pred_report_dir__
from digoie.core.ml.dataset.model import load_model
from digoie.core.ml.dataset.labeling import labeling
from operator import itemgetter 
import os

def predict(params):
    if 'string' in params:
        predict4string(params['string'])
    elif 'string' in params:
        print params['file']
    else:
        # defautl
        predict4dir()

def predict4dir(path=__pred_data_dir__):

    reverb_data = reverb.extract(path=path)
    if not len(reverb_data):
        raise Exception('nothing from reverb')
    featured = feature.extract(reverb_data)
    vectorized, predict_feature_names = vectorize(featured, my_min_df=0, my_max_df=1, update_feature_names=False)
    feature_names = load_feature_names()
    # vector = predict_vector(feature_names, predict_feature_names)
    # report(list(clf.predict([vector]))[0])
    
    labels = labeling(reverb_data)

    X = vectorized
    y = labels
    predict_feature_names = predict_feature_names.split(',')
    

    # predict4path(path, DECISION_TREE, feature_names, predict_feature_names, X, y)
    for mla in MACHINE_LEARNING_ALGORITHMS:
        predict4path(path, mla, feature_names, predict_feature_names, X, y)

def predict4path(path, mla, feature_names, predict_feature_names, X, y):
    # mla = AdaBoost
    clf = load_model(mla)

    predict_label = []
    target_label = []
    predict_X = []
    predict_y = []
    idx = 0
    for fn in X:
        # features = []
        tmp = [str(digit) for digit in list(fn)]
        # idxs = tmp.index('1')
        tmp = [i for i in range(len(tmp)) if tmp[i] == '1']
        tmp = itemgetter(*tmp)(predict_feature_names)
        tmp = ','.join(tmp) 
        vector = predict_vector(feature_names, tmp)
        # print vector
        predict = list(clf.predict([vector]))[0]
        target = y[idx]
        # print str(predict) + ' : ' + str(target)
        predict_X.append(vector)
        predict_y.append(str(predict) + ' : ' + str(target))
        predict_label.append(predict)
        target_label.append(target)
        idx += 1

    # """
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file

    yvec2file(predict_y, os.path.join(__ml_datasets_dir__, 'predict_y-' + mla ))
    features2file(predict_X, os.path.join(__ml_datasets_dir__, 'predict_X-' + mla), feature_names)

    # """

    print '#################################################################'
    print '#            ' + mla + ' report'
    print '#################################################################'
    print classification_report(target_label, predict_label)
    print 'accuracy: ' + str(accuracy_score(target_label, predict_label))
    print '\n\n'

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# need to fix
def predict4string(sentence):
    feature_names, X_train, X_test, y_train, y_test = generate_dataset()
    clf = generate_classifier(X_train, X_test, y_train, y_test)
    # clf = load_model(DECISION_TREE)   # decision_tree herefor test

    reverb_data = reverb.lauch4String(sentence)
    featured = extract(reverb_data)
    vectorized, predict_feature_names = vectorize(featured, my_min_df=0, my_max_df=1)

    vector = predict_vector(feature_names, predict_feature_names)

    report(list(clf.predict([vector]))[0])


# predict('My name is Jassica.')

def predict_vector(trained, predict):
    trained = trained.split(',')
    predict = predict.split(',')
    fn_length = len(trained)
    vector = [0] * fn_length
    for i in range(fn_length):
        if trained[i] in predict:
            vector[i] = 1
    return vector

# predict_vector()

def report(result):
    print '+--------------------------------------------------------+'
    print '|                     Predict Report                     +'
    print '+--------------------------------------------------------+'
    if result:
        print 'Contain name \n'
    else:
        print 'Does not contain name\n'

