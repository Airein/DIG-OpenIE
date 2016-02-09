
from sklearn.neighbors import KNeighborsClassifier


from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLKNeighbors(MLAlgorithm):

    # ML_NAME = K_NEIGHBORS

    def __init__(self, training_dataset, training_label):
        super(MLKNeighbors, self).__init__(training_dataset, training_label)

    def generate(self):
        classifier = KNeighborsClassifier(n_neighbors=3)
        super(MLKNeighbors, self).generate(classifier)
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return classifier

        






