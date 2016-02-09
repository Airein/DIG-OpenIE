
from operator import itemgetter 

def list2file(mylist, path, flag='wb'):
    fdp = open(path, flag)
    for item in mylist:
        fdp.writelines(item)



def features2file(mylist, path, feature_names, flag='wb'):
    fdp = open(path, flag)
    # print feature_names
    # print feature_names[0:2]
    feature_names = feature_names.split(',')
    for item in mylist:
        tmp = [str(digit) for digit in list(item)]
        tmp = [i for i in range(len(tmp)) if tmp[i] == '1']
        # tmp = feature_nammylist, path, path, feature_names, path, feature_nameses[tmp]
        tmp = itemgetter(*tmp)(feature_names)
        # tmp = feature_names[tmp.index('1')]
        # list2file(tmp, path)
        tmp = ','.join(tmp) 
        fdp.writelines(tmp + '\n')

def Xvec2file(mylist, path, flag='wb'):
    fdp = open(path, flag)
    for item in mylist:
        tmp = [str(digit) for digit in list(item)]
        # print tmp.index('1')
        tmp = ','.join(tmp) 
        fdp.writelines(tmp + '\n')

def yvec2file(mylist, path, flag='wb'):
    fdp = open(path, flag)
    for item in mylist:
        # print item
        # tmp = ','.join([str(digit) for digit in list(item)])
        fdp.writelines(str(item) + '\n')







