import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from digoie.conf.storage import __root_dir__

print __root_dir__