import os.path
import random
from ... import __root_dir__, __raw_outputs__, __reverb_outputs__, __data_folder__
from sklearn.feature_extraction.text import CountVectorizer
from . import FeatureExtractor

REVERB_OUTPUT = __root_dir__ + __reverb_outputs__ + 'reverb.output'
LABEL_DATA = __root_dir__ + __data_folder__ + 'ml/' + 'label.ml'
ML_DATA = __root_dir__ + __data_folder__ + 'ml/' + 'dataset.ml'
TRAIN_DATA = __root_dir__ + __data_folder__ + 'ml/' + 'train_data.ml'
TRAIN_LABEL = __root_dir__ + __data_folder__ + 'ml/' + 'train_label.ml'
TEST_DATA = __root_dir__ + __data_folder__ + 'ml/' + 'test_data.ml'
TEST_LABEL = __root_dir__ + __data_folder__ + 'ml/' + 'test_label.ml'
NAMES_OUTPUT = __root_dir__ + __raw_outputs__ + 'names.raw'



class MLDataLoader():
    def __init__(self):
        pass

    def load_feature_names(self):
        dataset_file = open(TRAIN_DATA, 'rU')
        for line in dataset_file:
            return line[:-1].split(',')

    def load_train_data(self):
        return self.load_dataset(TRAIN_DATA)

    def load_train_label(self):
        return self.load_label(TRAIN_LABEL)

    def load_test_data(self):
        return self.load_dataset(TEST_DATA)

    def load_test_label(self):
        return self.load_label(TEST_LABEL)

    def load_dataset(self, path):
        dataset_file = open(path, 'rU')
        data = list([data[:-1] for data in dataset_file])

        feature_names = data[0].split(',')
        dataset = data[1:]
        dataset = [[ int(data) for data in line.split(',')] for line in dataset]
        dataset_file.close()
        return (feature_names, dataset)

    def load_label(self, path):
        label_file = open(path, 'rU')
        label = [int(data) for data in list([data[:-1] for data in label_file])]
        return label










