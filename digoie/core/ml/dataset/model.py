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
    path = os.path.join(path, model_name + MODEL_EXT)
    joblib.dump(clf, path)

def load_model(model_name):
    path = os.path.join(__ml_models_dir__, model_name, model_name + MODEL_EXT)
    return joblib.load(path) 