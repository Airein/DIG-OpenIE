
"""
Author: Lingzhe Teng
Date:   Jan. 21, 2016

"""
import os


__title__ = "rvie"
__version__ = "0.0.1"
__license__ = "Apache 2.0"
__author__ = "Lingzhe Teng"

__root_dir__ = os.path.abspath(__file__ + "/../")  + '/'
__data_folder__ = 'data/'
__json_outputs__ = __data_folder__ + 'json/'
__raw_outputs__ = __data_folder__ + 'raw/'
__reverb_outputs__ = __data_folder__ + 'reverb/'


from .api import streams
from .api import parse
from .api import extract
from .api import RVIE_load_data
# from .session import ESstreamer