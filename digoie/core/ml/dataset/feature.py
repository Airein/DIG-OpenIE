

def extract(raw):
    print 'extract features...'
    featured = []
    for line in raw:
        line = line[:-1]
        line = line.split('\t')

        rvd_post = str(line[13]).split(' ')
        rvd_ct = str(line[14]).split(' ')
        
        rvd_arg1_val = str(line[15]).replace('.', '')
        rvd_arg1_start_idx = int(line[5])
        rvd_arg1_end_idx = int(line[6])

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

        rv4fe_data = ' '.join(var_list)
        featured.append(rv4fe_data)
    return featured


