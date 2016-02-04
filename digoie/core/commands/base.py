#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    digoie tcp <host> <port> [--timeout=<seconds>]
    digoie serial <port> [--baud=<n>] [--timeout=<seconds>]
    digoie (-i | --interactive)
    digoie (-h | --help | --version)
    digoie stream
    digoie parse
    digoie load
    digoie classifier
    digoie test

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""


from digoie.plugins.docopt import docopt, DocoptExit
from handler import *
from interactive import *

opt = docopt(__doc__, sys.argv[1:])
cmd_hander(opt)





# def get_command():
#     print 'get_command'

# def call_command():
#     pass
 
