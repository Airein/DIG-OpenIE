from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.ensemble import AdaBoostClassifier

# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier

class MLAdaBoost(MLAlgorithm):

    ML_NAME = AdaBoost

    def __init__(self):
        super(MLAdaBoost, self).__init__()

    def generate(self):
        classifier = AdaBoostClassifier()
        super(MLAdaBoost, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






