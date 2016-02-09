

import os
from digoie.utils.sys_info import *
from shutil import copyfile


##################################################################
#                             Path                               #  
##################################################################

## top-level
__root_dir__ = os.path.abspath(os.path.join(__file__,"..",".."))

__res_dir__ = os.path.join(__root_dir__, 'res')

## app path - user home dir
__app_dir__ = os.path.join(do_user_path(), 'dig_openie')

## res
__app_res_dir__ = os.path.join(__app_dir__, 'res')

## inside data dir
__app_data_dir__ = os.path.join(__app_dir__, 'data')

# elasticsearch data
__elastic_search_dir__ =os.path.join(__app_data_dir__, 'elasticsearch')

# reverb data
__reverb_dir__ = os.path.join(__app_data_dir__, 'reverb')
__reverb_input_dir__ = os.path.join(__reverb_dir__, 'input')
__reverb_output_dir__ = os.path.join(__reverb_dir__, 'output')

# machine learning data
__machine_learning_dir__ = os.path.join(__app_data_dir__, 'ml')
__ml_datasets_dir__ = os.path.join(__machine_learning_dir__, 'datasets')
__ml_models_dir__ = os.path.join(__machine_learning_dir__, 'models')

# predict data
__predict_dir__ = os.path.join(__app_data_dir__, 'predict')
__pred_data_dir__ = os.path.join(__predict_dir__, 'data')
__pred_report_dir__ = os.path.join(__predict_dir__, 'report')


STORAGE_PATH = [
                    __app_dir__,
                    __app_res_dir__,
                    __app_data_dir__,
                    __elastic_search_dir__,
                    __reverb_dir__,
                    __reverb_input_dir__,
                    __reverb_output_dir__,
                    __machine_learning_dir__,
                    __ml_datasets_dir__,
                    __ml_models_dir__,
                    __predict_dir__,
                    __pred_data_dir__,
                    __pred_report_dir__
                ]


##################################################################
#                             EXTS                               #  
##################################################################

ES_RAW_EXT = JSON_EXT = '.json'
REVERB_INPUT_EXT = '.rvi'
REVERB_OUTPUT_EXT = '.rvo'
ML_CLASSIFIER_EXT = '.clf'

##################################################################
#                             RES                                #  
##################################################################

# REVERB_RES = os.path.join(__res_dir__, 'reverb.jar')
REVERB_RES = 'reverb.jar'

STORAGE_RES =   [
            REVERB_RES
        ]
def storage_init():
    # path
    for path in STORAGE_PATH:
        if not os.path.exists(path):
             os.makedirs(path)

    # res
    for res in STORAGE_RES:
        path = os.path.join(__app_res_dir__, res)
        if not os.path.exists(path):
            src = os.path.join(__res_dir__, res)
            copyfile(src, path)












