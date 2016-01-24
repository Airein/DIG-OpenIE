# from .session import ESstreamer

from core import *


def RVIE_load_data():
    print '+--------------------------------------------------------+'
    print '|                        Load Data                       +'
    print '+--------------------------------------------------------+'
    streamer = ESstreamer()
    parser = JSparser()
    extractor = RVextractor()

    ""
    # fetch all names
    # streamer.fetch_names()
    names = parser.parseName()

    
    # fetch all sentences for each person
    # for name in names:
    #     streamer.fetch_sentences(name)
    # parser.parseSentence()

    data = extractor.extract(names)
    return data


def RVIE_analyze_data():
    print '+--------------------------------------------------------+'
    print '|                      Analyze Data                      +'
    print '+--------------------------------------------------------+'
    
    from sklearn import tree
    X = [['My name', 'is', 'Amber'], ['the type of girl', 'be willing as', 'you']]
    Y = [1, 0]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    print clf.predict([['my name', 'is', 'Amber']])



def streams():
    streamer = ESstreamer()
    streamer.streams()

def parse():
    parser = JSparser()
    # parser.parse()
    parser.parseName()

def extract():
    extractor = RVextractor()
    extractor.extract()


if __name__ == '__main__':
    pass