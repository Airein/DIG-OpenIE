from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.naive_bayes import GaussianNB

# http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB

class MLGaussianNaiveBayes(MLAlgorithm):

    ML_NAME = Gaussian_Naive_Bayes

    def __init__(self):
        super(MLGaussianNaiveBayes, self).__init__()

    def generate(self):
        classifier = GaussianNB()
        super(MLGaussianNaiveBayes, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






