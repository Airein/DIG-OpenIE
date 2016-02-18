import os
from digoie.core.parser.phoneno import parse_sentence
from digoie.conf.storage import __reverb_input_dir__, __elastic_search_dir__, REVERB_INPUT_EXT
from digoie.utils.symbols import do_newline_symbol


def stream():
    filename = 'phoneno.json'
    path = os.path.join(__elastic_search_dir__, filename)
    pn_file = open(path, 'rU')
    phoneno_json =  parse_sentence(pn_file)
    pn_file.close()

    filename = 'phoneno' + REVERB_INPUT_EXT
    path = os.path.join(__reverb_input_dir__, filename)
    sentence_file = open(path, 'wb')
    sentence_file.writelines(line + do_newline_symbol() for line in phoneno_json)
    sentence_file.close()

        


# stream()