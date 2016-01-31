from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn import tree



class MLDecisionTree(MLAlgorithm):

    ML_NAME = DECISION_TREE

    def __init__(self):
        super(MLDecisionTree, self).__init__()

    def generate(self):
        classifier = tree.DecisionTreeClassifier()
        super(MLDecisionTree, self).generate(classifier)
        # super(type, obj)
        save_model(self.ML_NAME, classifier)

        






