from ..plugin import api
from .. import __json_outputs__, __raw_outputs__, __reverb_outputs__, __root_dir__
from .utils import *


"""
Solution:
1. extract clean data from reverb output
2. run machine learning algorithm to train a classifier for name identification
3. In traning dataset, for all tokens in sentences that contain name, run tf-idf to filter end word


"""


class Classifier(object):
    def __init__(self):
        pass

    def train(self):
        pass

    def test(self):
        pass

    def preprocess(self):
        # generate dataset
        mldtGenerator = MLDataGenerator()
        mldtGenerator.generate()







        