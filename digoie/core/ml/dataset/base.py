
from digoie.conf.storage import __root_dir__, __reverb_output_dir__, REVERB_OUTPUT_EXT

from digoie.core.extractor.reverb import load_data
from digoie.core.ml.dataset.feature import extract

def generate_dataset():
    print 'generate dataset for machine learning...'

    reverb_data = load_data()
    extract(reverb_data)
    





