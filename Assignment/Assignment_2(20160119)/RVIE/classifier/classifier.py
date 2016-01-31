from ..plugin import api
from .. import __json_outputs__, __raw_outputs__, __reverb_outputs__, __root_dir__
from .utils import *
from .mla import *
from ..config import *

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

ML_MODEL_PATH = __root_dir__ + 'classifier/mla/models/'


class Classifier(object):
    def __init__(self):
        self.dataLoader = MLDataLoader()

    def generate_classifiers(self):
        # self.preprocess()
        # model = self.train(DECISION_TREE)
        # predict_label = classifier.test(DECISION_TREE)
        # classifier.report(predict_label)

        for mla in MACHINE_LEARNING_ALGORITHMS:
            (model, clf) = self.train(mla)

        # """
        feature_names, testing_dataset = self.dataLoader.load_test_data()

        for mla in MACHINE_LEARNING_ALGORITHMS:
            print 'Testing with classifier: ' + mla
            predict_label = self.test(mla, testing_dataset)
            self.report(predict_label)

        # """


    def preprocess(self):
        # generate dataset
        mldtGenerator = MLDataGenerator()
        mldtGenerator.generate()

    def train(self, mla=DECISION_TREE):
        print 'Begin to train classifier for... ' + mla

        if mla == DECISION_TREE:
            model = MLDecisionTree()
        elif mla == RANDOM_FOREST:
            model = MLRandomForest()
        elif mla == K_NEIGHBORS:
            model = MLKNeighbors()
        elif mla == SVM_SVC:
            model = MLSVC()
        elif mla == AdaBoost:
            model = MLAdaBoost()
        elif mla == Gaussian_Naive_Bayes:
            model = MLGaussianNaiveBayes()
        elif mla == Linear_Discriminant_Analysis:
            model = MLLinearDiscriminantAnalysis()
        elif mla == Quadratic_Discriminant_Analysis:
            model = MLQuadraticDiscriminantAnalysis()
        else:
            return None # test
        clf = model.generate()
        return (model, clf)


    def test(self, model_name=DECISION_TREE, testing_dataset=None):
        # return model.predict()
        if testing_dataset == None:
            feature_names, testing_dataset = self.dataLoader.load_test_data()
        
        clf = load_model(model_name)
        predict_label = list(clf.predict(testing_dataset))

        # test_label = self.dataLoader.load_test_label()  # test
        # feature_names, testing_dataset = self.dataLoader.load_test_data() # test
        # print clf.score(testing_dataset, test_label # test

        return predict_label

    def report(self, predict_label):
        test_label = self.dataLoader.load_test_label()
        # print 'predict_label: ' + str(predict_label)
        # print 'test_label: ' + str(test_label)
        print classification_report(test_label, predict_label)
        print 'accuracy: ' + str(accuracy_score(test_label, predict_label))
        print ''











        