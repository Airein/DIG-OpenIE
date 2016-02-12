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
    digoie dataset
    digoie classifier [--mla=<name>] [--min_df=<min_percent>] [--max_df=<max_percent>]
    digoie predict [--sentence=<string>]

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
    --mla=<name>  machine learning algorithms
"""


from digoie.plugins.docopt import docopt, DocoptExit
from digoie.apps.app import *
from handler import *
from interactive import *

app_init()
opt = docopt(__doc__, sys.argv[1:])
cmd_hander(opt)


# def get_command():
#     print 'get_command'

# def call_command():
#     pass
 
