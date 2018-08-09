from os.path import *
import os
import sys

_extdir = join(dirname(__file__), 'extension')
sys.path.append(_extdir)

os.chdir(_extdir)

from .extension import setup as _setup
