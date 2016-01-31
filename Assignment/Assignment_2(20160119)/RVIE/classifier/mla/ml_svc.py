from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.svm import SVC

# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC

class MLSVC(MLAlgorithm):

    ML_NAME = SVM_SVC

    def __init__(self):
        super(MLSVC, self).__init__()

    def generate(self):
        classifier = SVC()
        super(MLSVC, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






