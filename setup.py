from os.path import *
import os
import sys

_extdir = join(dirname(__file__), 'extension')
sys.path.append(_extdir)

os.chdir(_extdir)

import extension.setup
