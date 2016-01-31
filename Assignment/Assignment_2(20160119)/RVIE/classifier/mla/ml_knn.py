from ..utils import *
from ...config import *

from .mlalgorithm import MLAlgorithm
from sklearn.neighbors import KNeighborsClassifier



class MLKNeighbors(MLAlgorithm):

    ML_NAME = K_NEIGHBORS

    def __init__(self):
        super(MLKNeighbors, self).__init__()

    def generate(self):
        classifier = KNeighborsClassifier(n_neighbors=3)
        super(MLKNeighbors, self).generate(classifier)
        save_model(self.ML_NAME, classifier)

        






