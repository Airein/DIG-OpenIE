from ..plugin import api
from .. import __json_outputs__, __raw_outputs__, __reverb_outputs__, __root_dir__
from .utils import *
from .mla import *

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


class Classifier(object):
    def __init__(self):
        self.dataLoader = MLDataLoader()

    def train(self):
        print 'Begin to train classifier'

        decisionTree = MLDecisionTree()
        decisionTree.generate()
        return decisionTree


    def test(self, model=None):
        return model.predict()

    def report(self, predict_label):

        test_label = self.dataLoader.load_test_label()
        print 'predict_label: ' + str(predict_label)
        print 'test_label: ' + str(test_label)
        print classification_report(test_label, predict_label)
        print accuracy_score(test_label, predict_label)





    def preprocess(self):
        # generate dataset
        mldtGenerator = MLDataGenerator()
        mldtGenerator.generate()







        