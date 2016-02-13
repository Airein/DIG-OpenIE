
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from digoie.conf.machine_learning import DECISION_TREE, RANDOM_FOREST, MACHINE_LEARNING_ALGORITHMS, K_NEIGHBORS, SVM_SVC, AdaBoost, Gaussian_Naive_Bayes
from digoie.core.ml.dataset.model import save_model
from digoie.core.ml.classifier.mla.decision_tree import MLDecisionTree
from digoie.core.ml.classifier.mla.random_forest import MLRandomForest
from digoie.core.ml.classifier.mla.knn import MLKNeighbors
from digoie.core.ml.classifier.mla.svc import MLSVC
from digoie.core.ml.classifier.mla.ada_boost import MLAdaBoost
from digoie.core.ml.classifier.mla.gaussian_nb import MLGaussianNaiveBayes



def generate_classifier(X_train, X_test, y_train, y_test, mla=None):

    if mla == None:
        for mla in MACHINE_LEARNING_ALGORITHMS:
            print 'train ' + mla + ' classifier'
            clf = train(X_train, y_train, mla)
            test(X_test, y_test, mla, clf)
    else:
        clf = train(X_train, y_train, mla)
        test(X_test, y_test, mla, clf)
    # return clf

def train(X_train, y_train, mla=DECISION_TREE):
    # print 'train classifier'

    if mla == DECISION_TREE:
        model = MLDecisionTree(X_train, y_train)
    elif mla == RANDOM_FOREST:
        model = MLRandomForest(X_train, y_train)
    elif mla == K_NEIGHBORS:
        model = MLKNeighbors(X_train, y_train)
    elif mla == SVM_SVC:
        model = MLSVC(X_train, y_train)
    elif mla == AdaBoost:
        model = MLAdaBoost(X_train, y_train)
    elif mla == Gaussian_Naive_Bayes:
        model = MLGaussianNaiveBayes(X_train, y_train)
    # elif mla == Linear_Discriminant_Analysis:
    #     model = MLLinearDiscriminantAnalysis(X_train, y_train)
    # elif mla == Quadratic_Discriminant_Analysis:
    #     model = MLQuadraticDiscriminantAnalysis(X_train, y_train)
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
    print '\n\n'








