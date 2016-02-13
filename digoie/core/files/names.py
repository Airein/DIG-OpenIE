

import os
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, REVERB_INPUT_EXT


def load_names():
    names_list = []
    path = os.path.join(__elastic_search_dir__, 'names')
    names_file = open(path, 'rU')
    for line in names_file:
        name = line.split()
        # print name[0]
        names_list.append(name[0].lower())
        # break
    names_file.close()
    return names_list

# def load_names():
#     path = os.path.join(__elastic_search_dir__, 'names_bk')
#     names_file = open(path, 'rU')
#     names = list([name[:-1] for name in names_file])
#     names_file.close()
#     return names


# print ','.join(load_names())