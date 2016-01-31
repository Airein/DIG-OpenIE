from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# http://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis

class MLLinearDiscriminantAnalysis(MLAlgorithm):

    ML_NAME = Linear_Discriminant_Analysis

    def __init__(self):
        super(MLLinearDiscriminantAnalysis, self).__init__()

    def generate(self):
        classifier = LinearDiscriminantAnalysis()
        super(MLLinearDiscriminantAnalysis, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






