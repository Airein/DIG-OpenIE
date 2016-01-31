from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# http://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis

class MLQuadraticDiscriminantAnalysis(MLAlgorithm):

    ML_NAME = Quadratic_Discriminant_Analysis

    def __init__(self):
        super(MLQuadraticDiscriminantAnalysis, self).__init__()

    def generate(self):
        classifier = QuadraticDiscriminantAnalysis()
        super(MLQuadraticDiscriminantAnalysis, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






