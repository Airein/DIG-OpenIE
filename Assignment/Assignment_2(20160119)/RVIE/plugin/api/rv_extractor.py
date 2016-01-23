
import subprocess
import os.path

from ... import __root_dir__, __raw_outputs__, __reverb_outputs__


REVERB_EXEC_PATH = __root_dir__ + 'res/' + 'reverb-core-1.4.3-SNAPSHOT-jar-with-dependencies.jar'

class RVHelper():

    def __init__(self):
        pass

    def lauch_reverb(self, filename_list):
        # print REVERB_EXEC_PATH
        # print __root_dir__ + __reverb_outputs__ + 'reverb.output'
        path = __root_dir__ + __reverb_outputs__
        # print path
        filename = path + 'reverb.output'
        if os.path.isfile(filename):
            os.remove(filename)
        rv_output = open(filename, 'a')
        argsArray = ['java', '-Xmx512m', '-jar', REVERB_EXEC_PATH]
        argsArray.extend(filename_list)
        subprocess.call(argsArray, stdout=rv_output)


    def load_rv_data(self, filename=None):
        reverb_file = open(filename, 'rU')
        reverb_data = []
        for line in reverb_file:
            # row = str(line)
            line = line.split('\t')
            reverb_data.append(line)
        return reverb_data




