

import os
import re
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, REVERB_INPUT_EXT
from digoie.core.files.names import load_names


def labeling(reverb_data):
    print 'generate labels for machine learning...'
    # return label_name(reverb_data)
    return label_phone_number(reverb_data)


def label_name(reverb_data):
    names = load_names()
    label_list = []

    for line in reverb_data:
        line = line[:-1]
        line = line.split('\t')
        rvd_arg1_val = str(line[15]).replace('.', '')
        rvd_arg1_val = rvd_arg1_val.split(' ')

        rvd_arg2_val = str(line[17]).replace('.', '')
        rvd_arg2_val = rvd_arg2_val.split(' ')
        label = 0
        for name in names:
            name = name.lower()
            if name in rvd_arg1_val or name in rvd_arg2_val:                
                label = 1
                break;
        label_list.append(label)
    return label_list

def label_phone_number(reverb_data):
    label_list = []
    for line in reverb_data:
        line = line[:-1]

        line = line.split('\t')
        rvd_arg1_val = str(line[2])
        rvd_arg2_val = str(line[4])

        if has_phone_number(rvd_arg1_val) or has_phone_number(rvd_arg2_val):
            label_list.append(1)
        else:
            label_list.append(0)
    return label_list



def has_phone_number(string):
    reg = re.compile("\d{3}[+-._=:,\s]*\d{3}[+-._=:,\s]*\d{4}")
    # reg = re.compile('(zero|one|two|three|four|five|six|seven|eight|nine|\d|.){9}')
    return 1 if re.search(reg, string) else 0




"""
def label_phone_number(reverb_data):
    path = __reverb_input_dir__
    filename_list = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.split('.')[-1] == REVERB_INPUT_EXT[1:]]
    for file_path in filename_list:
        tmp_file = open(file_path, 'rU')
        for line in tmp_file:
            
            reg = re.compile("[0-9]{9pattern, string}")
            if re.match(reg, line):
                print line
"""

# test = 'Daniela please call 818.430.2219 P.S. i dont check.'
# test = 'If you like Please ? ? ? ? two.one.three.s'

test = '8.1.8.6.9.4.six.zero.four.eight.'

print 1 if has_phone_number(test) else 0






