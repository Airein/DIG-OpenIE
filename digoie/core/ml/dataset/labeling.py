

import os
import re
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, REVERB_INPUT_EXT
from digoie.core.files.names import load_names


def labeling(reverb_data):
    print 'generate labels for machine learning...'
    return label_name(reverb_data)
    # return label_phone_number(reverb_data)


def label_name(reverb_data):
    # load names
    names = load_names()
    label_list = []

    # used for test
    # custom_names = ['Sophia', 'Katie', 'Holly', 'Daniella', 'Natali', 'Colleen', 'Grace', 'Alina', 'Kylie', 'Lena', 'Monica', 'Hayes', 'Rachell', 'Brittany', 'Kendall', 'Merry', 'Jane', 'Vanessa', 'Ashlee', 'Ashley', 'Roxy', 'julie', 'Becky', 'keke', 'Brook', 'Sasha', 'Kayla', 'Lia', 'Moana', 'Lisa', 'Greek', 'Amoni', 'Jade', 'Juicy', 'sadie', 'Natalie', 'Libby', 'Mimi']
    # names.extend(custom_names)

    # rv4label_file = open(LABEL_DATA, 'wb')
    # i = 1
    for line in reverb_data:
        # print '--------------- line no: ' + str(i)
        # i+=1
        line = line[:-1]
        line = line.split('\t')
        rvd_arg1_val = str(line[15]).replace('.', '')
        # print 'rvd_arg1_val: ' + rvd_arg1_val
        rvd_arg1_val = rvd_arg1_val.split(' ')

        rvd_arg2_val = str(line[17]).replace('.', '')
        # print 'rvd_arg2_val: ' + rvd_arg2_val 
        rvd_arg2_val = rvd_arg2_val.split(' ')
        label = 0
        for name in names:
            # if name == 'Daniella':
            #     print 'Daniella here'
            name = name.lower()
            if name in rvd_arg1_val or name in rvd_arg2_val:
                # print name + ' in names'
                
                label = 1
                break;
        # rv4label_file.write(str(label) + '\n')
        label_list.append(label)
    # rv4label_file.close()
    return label_list



def label_phone_number(reverb_data):
    path = __reverb_input_dir__
    filename_list = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.split('.')[-1] == REVERB_INPUT_EXT[1:]]
    for file_path in filename_list:
        tmp_file = open(file_path, 'rU')
        for line in tmp_file:
            
            reg = re.compile("[0-9]{9pattern, string}")
            if re.match(reg, line):
                print line









