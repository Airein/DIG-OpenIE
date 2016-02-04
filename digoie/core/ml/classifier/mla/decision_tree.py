
from sklearn import tree


from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLDecisionTree(MLAlgorithm):

    # ML_NAME = DECISION_TREE

    def __init__(self, training_dataset, training_label):
        super(MLDecisionTree, self).__init__(training_dataset, training_label)

    def generate(self):
        classifier = tree.DecisionTreeClassifier()
        super(MLDecisionTree, self).generate(classifier)
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return classifier

        






