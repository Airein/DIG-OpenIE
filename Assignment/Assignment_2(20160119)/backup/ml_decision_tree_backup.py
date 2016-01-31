import os.path
from ... import __root_dir__, __raw_outputs__, __reverb_outputs__

from sklearn import tree
from ..utils import *
from ...config import *

# from sklearn.externals import joblib

ML_NAME = DECISION_TREE
ML_MODEL_PATH = __root_dir__ + 'classifier/mla/models/'

class MLDecisionTree():
    def __init__(self):
        self.classifier = None
        self.dataLoader = MLDataLoader()

    def generate(self, training_dataset=None, training_label=None):

        if training_dataset == None:
            feature_names, training_dataset = self.dataLoader.load_train_data()

        if training_label == None:
            training_label = self.dataLoader.load_train_label()  

        classifier = tree.DecisionTreeClassifier()
        classifier = classifier.fit(training_dataset, training_label)
        self.classifier = classifier
        save_model(ML_NAME, classifier)
        return classifier
        

    def predict(self, testing_dataset=None):
        if testing_dataset == None:
            feature_names, testing_dataset = self.dataLoader.load_test_data()
        
        # testing_label = self.dataLoader.load_test_label()
        # print training_dataset
        # print list(classifier.predict(testing_dataset))
        # print testing_label
        return list(self.classifier.predict(testing_dataset))

    # def save_model(self, clf):
    #     joblib.dump(clf, ML_MODEL_PATH + ML_NAME + '.pkl')

    # def load_model(self, model_name):
    #     return joblib.load(model_name + '.pkl') 




