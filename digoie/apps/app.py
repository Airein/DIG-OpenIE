
from digoie.utils.sys_info import *
from digoie.conf.storage import *

def app_init():
    # if do_isNT():
    #     print 'nt'
    # else:
    #     print 'unix'

    home = do_user_path()
    storage_init()
    

