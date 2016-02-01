

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
        # for publish
        # self.rv_extractor.lauch_reverb(filename_list)
        # for test
        print 'lauch reverb for files list: ' # + str(filename_list)
        print '... reverb output at ' + __reverb_outputs__ + 'reverb.output'
        # self.rv_extractor.lauch_reverb([filename_list[0], filename_list[1]])
        self.rv_extractor.lauch_reverb(filename_list)
        return self.rv_extractor.load_rv_data(__root_dir__ + __reverb_outputs__ + 'reverb.output')
