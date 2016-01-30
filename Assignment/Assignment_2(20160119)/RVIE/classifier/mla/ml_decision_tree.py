import os.path
from ... import __root_dir__, __raw_outputs__, __reverb_outputs__

from sklearn import tree
from ..utils import *

class MLDecisionTree():
    def __init__(self):
        pass

    def generate(self):
        dataLoader = MLDataLoader()
        feature_names, training_dataset = dataLoader.load_train_data()
        # print dataLoader.load_train_label()
        # print feature_names


