
import os

# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html
from sklearn.cross_validation import train_test_split

from digoie.conf.storage import __elastic_search_dir__
from digoie.core.extractor.reverb import load_data
from digoie.core.ml.dataset.feature import extract
from digoie.core.ml.dataset.vector import vectorize
from digoie.core.ml.dataset.labeling import labeling
from digoie.conf.global_settings import TARGET_PERSON_NAME, TARGET_PHONE_NUMBER

# test only

def generate_dataset(min_df, max_df, target=TARGET_PERSON_NAME):
    print 'generate dataset for machine learning...'

    reverb_data = load_data()
    labels = labeling(reverb_data)
    featured = extract(reverb_data, target=target)
    vectorized, feature_names = vectorize(featured, my_min_df=min_df, my_max_df=max_df)
    

    X = vectorized
    y = labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # print X
    # print '=========================='
    # print X_train

    """
     Test Only
     - used to analyse results
    """
    """
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file

    Xvec2file(X_train, os.path.join(__ml_datasets_dir__, 'X_train'))
    Xvec2file(X_test, os.path.join(__ml_datasets_dir__, 'X_test'))
    yvec2file(y_train, os.path.join(__ml_datasets_dir__, 'y_train'))
    yvec2file(y_test, os.path.join(__ml_datasets_dir__, 'y_test'))

    features2file(X_train, os.path.join(__ml_datasets_dir__, 'X_train_features'), feature_names)
    features2file(X_test, os.path.join(__ml_datasets_dir__, 'X_test_features'), feature_names)
    """

    return feature_names, X_train, X_test, y_train, y_test













