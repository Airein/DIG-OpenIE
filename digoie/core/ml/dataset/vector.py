import re
import os
from sklearn.feature_extraction.text import CountVectorizer


from digoie.conf.storage import __root_dir__, __ml_datasets_dir__
from digoie.utils.symbols import do_newline_symbol





def vectorize(raw, my_min_df=0.0005, my_max_df=0.5, update_feature_names=True):
    print 'build vector for features...'
    print 'min_df: ' + str(my_min_df)
    print 'max_df: ' + str(my_max_df)
    vectorizer = CountVectorizer(tokenizer=custom_tokenizer, min_df=float(my_min_df), max_df=float(my_max_df))
    dataset = vectorizer.fit_transform(raw).toarray()

    # write feature names
    print 'extract feature names for vector...'
    feature_names = [x.encode('UTF8') for x in vectorizer.get_feature_names()]
    feature_names = ','.join([name for name in feature_names])

    if update_feature_names:
        print 'update_feature_names..'
        path = os.path.join(__ml_datasets_dir__, 'feature_names')
        feature_names_file = open(path, 'wb')
        feature_names_file.writelines(line + do_newline_symbol() for line in feature_names.split(','))
        feature_names_file.close()
    return (dataset, feature_names)

def custom_tokenizer(raw):
    raw_list = raw.split()
    result = []
    reg_tag = re.compile("^[oOpPsS]4(\w*|\w2\w*)$")
    tags = [word for word in raw_list if re.match(reg_tag, word)]
    reg_name = re.compile("^[a-zA-Z]+$")
    words = [word for word in raw_list if re.match(reg_name, word)]
    reg_others = re.compile("^[#]+$")
    others = [word for word in raw_list if re.match(reg_others, word)]
    result.extend(tags)
    result.extend(words)
    result.extend(others)
    return result

def load_feature_names():
    path = os.path.join(__ml_datasets_dir__, 'feature_names')
    feature_names_file = open(path, 'rU')
    names = [name[:-1] for name in list(feature_names_file)]
    # print len(namesobject)
    names = ','.join(names)
    return names


