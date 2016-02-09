
import os

# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html
from sklearn.cross_validation import train_test_split

from digoie.conf.storage import __elastic_search_dir__
from digoie.core.extractor.reverb import load_data
from digoie.core.ml.dataset.feature import extract
from digoie.core.ml.dataset.vector import vectorize

def generate_dataset():
    print 'generate dataset for machine learning...'

    
    reverb_data = load_data()
    featured = extract(reverb_data)
    vectorized, feature_names = vectorize(featured)
    labels = labeling(reverb_data)

    X = vectorized
    y = labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return feature_names, X_train, X_test, y_train, y_test



def labeling(reverb_data):
    print 'generate labels for machine learning...'

    # load names
    path = os.path.join(__elastic_search_dir__, 'names')
    names_file = open(path, 'rU')
    names = list([name[:-1] for name in names_file])
    names_file.close()
    label_list = []

    # used for test
    custom_names = ['Sophia', 'Katie', 'Holly', 'Daniella', 'Natali', 'Colleen', 'Grace', 'Alina', 'Kylie', 'Lena']

    names.extend(custom_names)

    # rv4label_file = open(LABEL_DATA, 'wb')
    for line in reverb_data:
        line = line[:-1]
        line = line.split('\t')
        rvd_arg1_val = str(line[15]).replace('.', '')
        rvd_arg2_val = str(line[17]).replace('.', '')
        label = 0
        for name in names:
            if name in rvd_arg1_val or name in rvd_arg2_val:
                label = 1
                break;
        # rv4label_file.write(str(label) + '\n')
        label_list.append(label)
    # rv4label_file.close()
    return label_list










