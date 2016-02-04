"""ReVerb Information Extraction

Last Run
Summary: 61055 extractions, 104808 sentences, 496 files, 287 seconds
"""

import os
import subprocess

from digoie.conf.storage import __root_dir__, __app_res_dir__, __reverb_input_dir__, __reverb_output_dir__, REVERB_INPUT_EXT, REVERB_OUTPUT_EXT, REVERB_RES


##################################################################
#                            Extract                             #  
##################################################################

def extract():
    path = __reverb_input_dir__
    filename_list = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.split('.')[-1] == REVERB_INPUT_EXT[1:]]
    filename = 'reverb' + REVERB_OUTPUT_EXT
    path = os.path.join(__reverb_output_dir__, filename)
    if os.path.isfile(path):
        os.remove(path)
    lauch(filename_list, path)
    
def lauch(flist, path):
    rv_output_file = open(path, 'a')
    argsArray = ['java', '-Xmx512m', '-jar', load_executor()]
    argsArray.extend(flist)
    subprocess.call(argsArray, stdout=rv_output_file)
    rv_output_file.close()

def load_executor():
    # REVERB_EXEC = 'reverb.jar' # os.path.join(__root_dir__, 'res', 'reverb.jar')
    reverb = os.path.join(__app_res_dir__, REVERB_RES)
    # reverb = os.path.abspath(os.path.join(__file__,"..", REVERB_EXEC))
    return reverb

##################################################################
#                             Load                               #  
##################################################################

def load_data(path=None):
    print 'load data from reverb output...'
    filename = 'reverb' + REVERB_OUTPUT_EXT
    if path == None:
        path = os.path.join(__reverb_output_dir__, filename)
    reverb_file = open(path)
    reverb_data = []
    for line in reverb_file:
        # rv4fe_data = self.load_rv4line(line)
        reverb_data.append(line)
    reverb_file.close()
    return reverb_data


