import os, errno
from sklearn.externals import joblib
from ... import __root_dir__, __raw_outputs__, __reverb_outputs__, __data_folder__

ML_MODEL_PATH = __root_dir__ + 'classifier/mla/models/'

def save_model(model_name, clf):
    # os.remove(model_name) if os.path.exists(model_name) else None
    path = ML_MODEL_PATH + model_name + '/'
    if not os.path.exists(path):
        os.makedirs(path)
    joblib.dump(clf, path + model_name + '.pkl')

def load_model(model_name):
    path = ML_MODEL_PATH + model_name + '/'
    return joblib.load(path + model_name + '.pkl') 