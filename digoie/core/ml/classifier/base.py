
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from digoie.conf.machine_learning import DECISION_TREE, RANDOM_FOREST
from digoie.core.ml.dataset.model import save_model
from digoie.core.ml.classifier.mla.decision_tree import MLDecisionTree
from digoie.core.ml.classifier.mla.random_forest import MLRandomForest


def generate_classifier(X_train, X_test, y_train, y_test, mla=DECISION_TREE):
    clf = train(X_train, y_train, mla)
    test(X_test, y_test, mla, clf)
    return clf

def train(X_train, y_train, mla=DECISION_TREE):
    print 'train classifier'

    if mla == DECISION_TREE:
        model = MLDecisionTree(X_train, y_train)
    elif mla == RANDOM_FOREST:
        model = MLRandomForest(X_train, y_train)
    # elif mla == K_NEIGHBORS:
    #     model = MLKNeighbors()
    # elif mla == SVM_SVC:
    #     model = MLSVC()
    # elif mla == AdaBoost:
    #     model = MLAdaBoost()
    # elif mla == Gaussian_Naive_Bayes:
    #     model = MLGaussianNaiveBayes()
    # elif mla == Linear_Discriminant_Analysis:
    #     model = MLLinearDiscriminantAnalysis()
    # elif mla == Quadratic_Discriminant_Analysis:
    #     model = MLQuadraticDiscriminantAnalysis()
    else:
        return None # test
    clf = model.generate()
    save_model(mla, clf)
    return clf # (model, clf) 

def test(X_test, y_test, mla, clf):
    predict_label = list(clf.predict(X_test))
    target_label = y_test
    
    print '+--------------------------------------------------------+'
    print '|                   Classifier Report                    +'
    print '+--------------------------------------------------------+'
    print 'Classifier: ' + mla
    print classification_report(target_label, predict_label)
    print 'accuracy: ' + str(accuracy_score(target_label, predict_label))








