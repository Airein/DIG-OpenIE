import os


def do_user_path():
    from os.path import expanduser
    home = expanduser("~")
    return home


def do_platform():
    if os.name == 'nt': # Windows
        return 'windows'
        # basePath = 'C:\\working\\'
    else:
        return 'unix'
        # basePath = '/working/'

def do_isNT():
    if do_platform() == 'nt':
        return True
    else:
        return False


