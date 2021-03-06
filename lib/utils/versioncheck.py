#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
Use as 'from lib.utils import versioncheck'
It has to be the first non-standard import before your project enter main() function
"""

import sys

PYVERSION = sys.version.split()[0]

if PYVERSION < "2.7":
    exit("[CRITICAL] incompatible Python version detected ('%s'). "
         "For successfully running this project, you'll have to use version >= 2.7"
         "(visit 'http://www.python.org/download/')" % PYVERSION)

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
