
from digoie.utils.sys_info import *


def do_newline_symbol():
    if do_isNT():
        return '\r\n'
    else:
        return '\n'
