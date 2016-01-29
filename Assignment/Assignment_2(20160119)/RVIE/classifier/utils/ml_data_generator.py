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



class MLDataGenerator():
    def __init__(self):
        pass

    def load_names(self):
        names_file = open(NAMES_OUTPUT, 'rU')
        names = list([name[:-1] for name in names_file])
        names_file.close()
        return names

    def generate(self):
        # self.generate_dataset()
        # self.generate_label()
        self.generate4ml(.8)

    def generate4ml(self, train_test_rate=.8):
        rv4ml_file = open(ML_DATA, 'rU')
        rv4label_file = open(LABEL_DATA, 'rU')

        data = list([data[:-1] for data in rv4ml_file])
        label = list([label[:-1] for label in rv4label_file])

        feature_names = data[0]
        dataset = data[1:]
        num_lines = len(label)
        # num_lines = sum(1 for line in rv4label_file)
        # print random.sample(data[1:], int(train_test_rate*num_lines)) 
        
        idx_list = list(xrange(num_lines))
        random.shuffle(idx_list)
        split_idx = int(train_test_rate*num_lines)
        idx4train = idx_list[:split_idx]
        idx4test = idx_list[split_idx:]

        # dataset[idx4train]
        train_data_file = open(TRAIN_DATA, 'wb')
        train_label_file = open(TRAIN_LABEL, 'wb')
        test_data_file = open(TEST_DATA, 'wb')
        test_label_file = open(TEST_LABEL, 'wb')

        # feature_names = ','.join([name for name in feature_names])

        # write training data
        train_data_file.write(feature_names + '\n')
        for idx in idx4train:
            train_data_file.write(dataset[idx] + '\n')
            train_label_file.write(label[idx] + '\n')


        # write testing data
        test_data_file.write(feature_names + '\n')
        for idx in idx4test:
            test_data_file.write(dataset[idx] + '\n')
            test_label_file.write(label[idx] + '\n')

        

        train_data_file.close()
        train_label_file.close()
        test_data_file.close()
        test_label_file.close()

        rv4ml_file.close()
        rv4label_file.close()

    def generate_dataset(self):
        rv4ml_file = open(ML_DATA, 'wb')

        # feature extraction
        featureExtractor = FeatureExtractor()
        fe_data = featureExtractor.extract()
        
        # text feature extraction
        vectorizer = CountVectorizer()
        # vectorizer = CountVectorizer(analyzer="word", token_pattern="((\"[^\"]+?\")|('[^']+?')|([^\\s]+?))\\s++")
        vectorizer.get_params()
        
        dataset = vectorizer.fit_transform(fe_data).toarray()
        feature_names = [x.encode('UTF8') for x in vectorizer.get_feature_names()]

        # write feature names
        feature_names = ','.join([name for name in feature_names])
        rv4ml_file.write(feature_names + '\n')

        # write dataset
        for line in dataset:
            line = ','.join([str(digit) for digit in line])
            rv4ml_file.write(line + '\n')
        rv4ml_file.close()

        # print dataset[0]
        # X_2 = dataset.toarray()
        # print X_2[-2]
        # print [x.encode('UTF8') for x in vectorizer.get_feature_names()]
        # print vectorizer.get_feature_names()
        




    def generate_label(self):
        reverb_file = open(REVERB_OUTPUT, 'rU')
        rv4label_file = open(LABEL_DATA, 'wb')
        names = self.load_names()
        label_list = []
        for line in reverb_file:
            line = line[:-1]
            line = line.split('\t')
            rvd_arg1_val = str(line[15]).replace('.', '')
            # rvd_rel_val  = str(line[16]).replace('.', '')
            rvd_arg2_val = str(line[17]).replace('.', '')
            label = 0
            # print rvd_arg2_val
            # [label = 1 for name in names if name in rvd_arg1_val or name in rvd_arg2_val]
            for name in names:
                if name in rvd_arg1_val or name in rvd_arg2_val:
                    label = 1
                    break;
            rv4label_file.write(str(label) + '\n')
            label_list.append(label)
        reverb_file.close()
        rv4label_file.close()
        return label_list



