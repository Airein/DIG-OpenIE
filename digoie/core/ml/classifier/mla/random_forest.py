
from sklearn.ensemble import RandomForestClassifier

from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLRandomForest(MLAlgorithm):

    # ML_NAME = RANDOM_FOREST

    def __init__(self, training_dataset, training_label):
        super(MLRandomForest, self).__init__(training_dataset, training_label)

    def generate(self):
        classifier = RandomForestClassifier()
        super(MLRandomForest, self).generate(classifier)
        # save_model(self.ML_NAME, classifier)
        return classifier

        






