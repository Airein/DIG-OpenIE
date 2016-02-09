
from sklearn.svm import SVC


from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLSVC(MLAlgorithm):

    # ML_NAME = K_NEIGHBORS

    def __init__(self, training_dataset, training_label):
        super(MLSVC, self).__init__(training_dataset, training_label)

    def generate(self):
        classifier = SVC()
        super(MLSVC, self).generate(classifier)
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return classifier

        






