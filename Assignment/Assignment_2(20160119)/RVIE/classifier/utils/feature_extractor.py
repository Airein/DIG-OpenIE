import os.path
from ... import __root_dir__, __raw_outputs__, __reverb_outputs__

from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction.text import TfidfTransformer

REVERB_OUTPUT = __root_dir__ + __reverb_outputs__ + 'reverb.output'

# ReVerb data for feature extraction
FE_RV_DATA = __root_dir__ + __reverb_outputs__ + 'rv4fe.output'


class FeatureExtractor():
    def __init__(self):
        pass

    def extract(self):
        print 'begin to extract feature from ReVerb output'
        rv4fe_data = self.load_reverb_data()
        return rv4fe_data

    def load_reverb_data(self):
        reverb_file = open(REVERB_OUTPUT, 'rU')
        rv4fe_file = open(FE_RV_DATA, 'wb')
        # rv4fe_index = [13,14,15,16,17]   # index for reverb output
        reverb_data = []

        for line in reverb_file:
            rv4fe_data = self.load_rv4line(line)
            rv4fe_file.write(rv4fe_data + '\n')
            # rv4fe_data = rv4fe_data.split(' ')
            # print rv4fe_data
            reverb_data.append(rv4fe_data)
            
        rv4fe_file.close()
        # print reverb_data
        return reverb_data


    def load_rv4line(self, line):
        line = line[:-1]
        line = line.split('\t')
        # print line
        rvd_post = str(line[13]).split(' ')
        rvd_ct = str(line[14]).split(' ')
        
        rvd_arg1_val = str(line[15]).replace('.', '')
        rvd_arg1_start_idx = int(line[5])
        rvd_arg1_end_idx = int(line[6])

        # rvd_arg1_post_tags = rvd_post[rvd_arg1_start_idx:rvd_arg1_end_idx]
        # rvd_arg1_post_tags = ['S_' + s for s in rvd_arg1_post_tags]
        # rvd_arg1_post_tags = ' '.join(rvd_arg1_post_tags)
        
        # rvd_arg1_ct_tags = ' '.join(rvd_ct[rvd_arg1_start_idx:rvd_arg1_end_idx])
        # rvd_arg1_ct_tags = ['S_' + s for s in rvd_arg1_ct_tags]

        rvd_rel_val  = str(line[16]).replace('.', '')
        rvd_rel_start_idx = int(line[7])
        rvd_rel_end_idx = int(line[8])

        rvd_arg2_val = str(line[17]).replace('.', '')
        rvd_arg2_start_idx = int(line[9])
        rvd_arg2_end_idx = int(line[10])

        # load post and chunk tags
        rvd_arg1_post_tags = rvd_post[rvd_arg1_start_idx:rvd_arg1_end_idx]
        rvd_arg1_ct_tags = rvd_ct[rvd_arg1_start_idx:rvd_arg1_end_idx]

        rvd_rel_post_tags = rvd_post[rvd_rel_start_idx:rvd_rel_end_idx]
        rvd_rel_ct_tags = rvd_ct[rvd_rel_start_idx:rvd_rel_end_idx]

        rvd_arg2_post_tags = rvd_post[rvd_arg2_start_idx:rvd_arg2_end_idx]
        rvd_arg2_ct_tags = rvd_ct[rvd_arg2_start_idx:rvd_arg2_end_idx]

        # format chunk tags
        rvd_arg1_ct_tags = [tag.replace('-','2') for tag in rvd_arg1_ct_tags]
        rvd_rel_ct_tags = [tag.replace('-','2') for tag in rvd_rel_ct_tags]
        rvd_arg2_ct_tags = [tag.replace('-','2') for tag in rvd_arg2_ct_tags]


        # add prefix for tags
        prefix = 'S4'
        rvd_arg1_post_tags = [prefix + elt for elt in rvd_arg1_post_tags]
        rvd_arg1_ct_tags = [prefix + elt for elt in rvd_arg1_ct_tags]

        prefix = 'P4'
        rvd_rel_post_tags = [prefix + elt for elt in rvd_rel_post_tags]
        rvd_rel_ct_tags = [prefix + elt for elt in rvd_rel_ct_tags]

        prefix = 'O4'
        rvd_arg2_post_tags = [prefix + elt for elt in rvd_arg2_post_tags]
        rvd_arg2_ct_tags = [prefix + elt for elt in rvd_arg2_ct_tags]

        # count same tags
        """
        self.count_tags(rvd_arg1_post_tags)
        self.count_tags(rvd_arg1_ct_tags)

        self.count_tags(rvd_rel_post_tags)
        self.count_tags(rvd_rel_ct_tags)

        self.count_tags(rvd_arg2_post_tags)
        self.count_tags(rvd_arg2_ct_tags)
        """
        
        # print rvd_arg2_post_tags


        # transfer list into string
        rvd_arg1_post_tags = ' '.join(rvd_arg1_post_tags)
        rvd_arg1_ct_tags = ' '.join(rvd_arg1_ct_tags)

        rvd_rel_post_tags = ' '.join(rvd_rel_post_tags)
        rvd_rel_ct_tags = ' '.join(rvd_rel_ct_tags)

        rvd_arg2_post_tags = ' '.join(rvd_arg2_post_tags)
        rvd_arg2_ct_tags = ' '.join(rvd_arg2_ct_tags)


        var_list = [
                        rvd_arg1_val, 
                        rvd_arg1_post_tags, 
                        rvd_arg1_ct_tags,
                        rvd_rel_val, 
                        rvd_rel_post_tags, 
                        rvd_rel_ct_tags,
                        rvd_arg2_val, 
                        rvd_arg2_post_tags, 
                        rvd_arg2_ct_tags
                    ]

        # print str(var_list)
        rv4fe_data = ' '.join(var_list)
        return rv4fe_data
        # rv4fe_data = rvd_arg1 + ' ' + rvd_rel + ' ' + rvd_arg2 + ' '

        """
        for idx in range(len(line)):
            if idx in rv4fe_index:
                if idx == 15 or idx == 12:
                    rv4fe_data += '\n'
                rv4fe_data += line[idx].encode('utf-8').strip() + '\t\t'
                if idx == 17:
                    rv4fe_data += '\n'
        """

    def count_tags(self, tag_list):
        tag_dict = {}
        for tag in tag_list:
            tag_dict.setdefault(tag, 0)
            tag_dict[tag] += 1
        # print tag_dict

        tag_list[:] =[]

        for (k, v) in tag_dict.items():
            tag_list.append(k + '_' + str(v))
            # if v == 1:
            #     tag_list.append(k)
            # else:
            #     for i in range(1,v+1):
            #         tag_list.append(k + '_' + str(i))
        # print result
        return tag_list









