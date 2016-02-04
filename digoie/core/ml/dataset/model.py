import os, errno
from sklearn.externals import joblib

from digoie.conf.storage import __ml_models_dir__

# ML_MODEL_PATH = __root_dir__ + 'classifier/mla/models/'
MODEL_EXT = '.pkl'

def save_model(model_name, clf):
    # os.remove(model_name) if os.path.exists(model_name) else None
    path = os.path.join(__ml_models_dir__, model_name)
    if not os.path.exists(path):
        os.makedirs(path)
    joblib.dump(clf, path + model_name + MODEL_EXT)

def load_model(model_name):
    path = os.path.join(__ml_models_dir__, model_name)
    return joblib.load(path + model_name + MODEL_EXT) 