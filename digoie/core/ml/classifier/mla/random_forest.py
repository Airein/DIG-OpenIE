from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.ensemble import RandomForestClassifier


class MLRandomForest(MLAlgorithm):

    ML_NAME = RANDOM_FOREST

    def __init__(self):
        super(MLRandomForest, self).__init__()

    def generate(self):
        classifier = RandomForestClassifier()
        super(MLRandomForest, self).generate(classifier)
        save_model(self.ML_NAME, classifier)
        return classifier

        






