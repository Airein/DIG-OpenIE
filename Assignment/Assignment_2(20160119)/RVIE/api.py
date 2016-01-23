# from .session import ESstreamer

from core import *


def RVIE_load_data():
    streamer = ESstreamer()
    parser = JSparser()
    extractor = RVextractor()

    
    # fetch all names
    # streamer.fetch_names()
    names = parser.parseName()

    """
    # fetch all sentences for each person
    for name in names:
        streamer.fetch_sentences(name)
    parser.parseSentence()
    """

    data = extractor.extract(names)
    print data[0]






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