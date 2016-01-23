

from ..plugin import api
from .. import __json_outputs__, __raw_outputs__, __reverb_outputs__, __root_dir__


class RVextractor(object):
    def __init__(self):
        self.rv_extractor = api.RVHelper()

    def extract(self, names=None):
        path = __root_dir__ + __raw_outputs__ + 'sentences/'
        filename_list = []
        if not names:
            rv_input = path + 'sentences.raw'
            rv_output = 'reverb.output'
        else:
            # print names
            for name in names:
                # print name
                filename_list.append(path + str(name) + '.raw')
            # namefile_string = '.raw\t'.join(path + str(x) for x in names)
            # print namefile_string
            # rv_input = path + name + '.raw'
            # rv_output = name + '.output'
        # print name_list
        # filename = namefile_string
        # self.rv_extractor.lauch_reverb(filename_list)
        self.rv_extractor.lauch_reverb([filename_list[0], filename_list[1]])
        return self.rv_extractor.load_rv_data(__root_dir__ + __reverb_outputs__ + 'reverb.output')
