# from .session import ESstreamer

from core import *
from classifier import *
from .config import *

streamer = ESstreamer()
parser = JSparser()
extractor = RVextractor()
classifier = Classifier()

def RVIE_load_data():
    print '+--------------------------------------------------------+'
    print '|                        Load Data                       +'
    print '+--------------------------------------------------------+'
    # streamer = ESstreamer()
    # parser = JSparser()
    # extractor = RVextractor()

    # fetch all names
    names = load_names()

    
    # fetch all sentences for each person
    load_sentences()

    # extract data
    data = rv_extract(names)
    return data

def load_names():
    print 'begin to load names'
    streamer.fetch_names()
    names = parser.parseName()
    return names

def load_sentences(names):
    print 'begin to fetch sentences'
    for name in names:
        streamer.fetch_sentences(name)
    parser.parseSentence()

def rv_extract(names):
    print 'begin to extract by ReVerb'
    data = extractor.extract(names)
    return data




def RVIE_analyze_data():
    print '+--------------------------------------------------------+'
    print '|                      Analyze Data                      +'
    print '+--------------------------------------------------------+'
    
    """
    from sklearn import tree
    X = [['My name', 'is', 'Amber'], ['the type of girl', 'be willing as', 'you']]
    Y = [1, 0]
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = clf.fit(X, Y)
    print clf.predict([['my name', 'is', 'Amber']])
    # model = classifier.train()
    # predict_label = classifier.test(DECISION_TREE)
    # classifier.report(predict_label)
    """

    # classifier.preprocess()
    classifier.generate_classifiers()

    
    

####################################################################
#                               TEST                               #
####################################################################

def streams():
    streamer = ESstreamer()
    streamer.fetch_names()

def parse():
    parser = JSparser()
    names = parser.parseName()
    return names

def extract():
    extractor = RVextractor()
    extractor.extract()


if __name__ == '__main__':
    pass