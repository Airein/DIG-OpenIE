import re
import os
from sklearn.feature_extraction.text import CountVectorizer


from digoie.conf.storage import __root_dir__, __ml_datasets_dir__
from digoie.utils.symbols import do_newline_symbol
from operator import itemgetter 
import numpy as np


def vectorize(raw, my_min_df=0.0005, my_max_df=0.5, update_feature_names=True):
    print 'build vector for features...'
    print 'min_df: ' + str(my_min_df)
    print 'max_df: ' + str(my_max_df)

    sw = ['digoieseparator']
    max_features = 10000
    vectorizer = CountVectorizer(analyzer='word', stop_words=sw, tokenizer=custom_tokenizer, min_df=float(my_min_df), max_df=float(my_max_df), max_features=max_features, ngram_range=(1,1))
    dataset = vectorizer.fit_transform(raw).toarray()

    # write feature names
    # print 'extract feature names for vector...'
    feature_names = [x.encode('UTF8') for x in vectorizer.get_feature_names()]
    # dataset, feature_names = vectorizer_filter(dataset, feature_names)
    feature_names = ','.join([name for name in feature_names])

    if update_feature_names:
        print 'update_feature_names..'
        path = os.path.join(__ml_datasets_dir__, 'feature_names')
        feature_names_file = open(path, 'wb')
        feature_names_file.writelines(line + do_newline_symbol() for line in feature_names.split(','))
        feature_names_file.close()
    return (dataset, feature_names)

def custom_tokenizer(raw):
    # print 'raw:  ' + raw

    raw_list = raw.split()
    # if 'digoieseparator' in raw_list:
    #     return []

    result = []
    reg_tag = re.compile("^[oOpPsS]4(\w*|\w2\w*)$")
    tags = [word for word in raw_list if re.match(reg_tag, word)]
    reg_name = re.compile("^[a-zA-Z]+$")
    words = [word for word in raw_list if re.match(reg_name, word)]
    reg_others = re.compile("^([#]+|conf[0-9])$")
    others = [word for word in raw_list if re.match(reg_others, word)]
    result.extend(words)
    result.extend(tags)
    result.extend(others)
    # print 'result: ' + str(result)
    return result

def load_feature_names():
    path = os.path.join(__ml_datasets_dir__, 'feature_names')
    feature_names_file = open(path, 'rU')
    names = [name[:-1] for name in list(feature_names_file)]
    # print len(namesobject)
    names = ','.join(names)
    return names



def vectorizer_filter(dataset, feature_names):
    sws = ['digoieseparator']
    reg = re.compile("conf[0-9]")
    feature_idx = []
    feature_idx_rm = []
    for i in range(len(feature_names)):
        feature = feature_names[i]
        useit = True
        if re.search(reg, feature):
            useit = False
        for sw in sws:
            if sw in feature:
                useit = False
                break
        if useit:
            feature_idx.append(i)
        else:
            feature_idx_rm.append(i)

    feature_names = itemgetter(*feature_idx)(feature_names)
    # print '\n'.join(feature_names)
    dataset = np.delete(dataset, np.s_[feature_idx_rm], 1)
    return dataset, feature_names        




"""
# sw = ['digoieseparator']
# analyzer='word', stop_words=sw, 
v = CountVectorizer(tokenizer=custom_tokenizer, ngram_range=(2, 2))
# raw_doc = v.fit(["my limitless skills talents have digoieseparator conf0 digoieseparator s4prp$ s4jj s4nns s4cc s4nns p4md p4vb o4prp digoieseparator s4b2np s4i2np s4i2np s4i2np s4i2np p4b2vp p4i2vp o4b2np"]).vocabulary_
# dataset = v.transform(raw_doc)



# print raw_doc
# print dataset.toarray()

dataset = v.fit_transform(["my limitless skills talents have digoieseparator conf0 digoieseparator s4prp$ s4jj s4nns s4cc s4nns p4md p4vb o4prp digoieseparator s4b2np s4i2np s4i2np s4i2np s4i2np p4b2vp p4i2vp o4b2np"]).toarray()
feature_names = [x.encode('UTF8') for x in v.get_feature_names()]

dataset, feature_names = vectorizer_filter(dataset, feature_names)
print '\n'.join(feature_names)

"""



    




