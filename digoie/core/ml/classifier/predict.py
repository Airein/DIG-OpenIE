

from digoie.core.ml.dataset.model import load_model
from digoie.conf.machine_learning import DECISION_TREE, RANDOM_FOREST
from digoie.core.extractor.reverb import lauch4String
from digoie.core.ml.dataset.feature import extract
from digoie.core.ml.dataset.vector import vectorize
from digoie.core.ml.dataset.base import generate_dataset
from digoie.core.ml.classifier.base import generate_classifier

def predict(sentence):
    feature_names, X_train, X_test, y_train, y_test = generate_dataset()
    clf = generate_classifier(X_train, X_test, y_train, y_test)
    # clf = load_model(DECISION_TREE)   # decision_tree herefor test

    reverb_data = lauch4String(sentence)
    featured = extract(reverb_data)
    vectorized, predict_feature_names = vectorize(featured, my_min_df=0, my_max_df=1)

    vector = predict_vector(feature_names, predict_feature_names)

    print '+--------------------------------------------------------+'
    print '|                     Predict Report                     +'
    print '+--------------------------------------------------------+'
    if list(clf.predict([vector]))[0]:
        print 'Contain name at sentence: \n' + sentence
    else:
        print 'Does not contain name at sentence: \n' + sentence



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

