#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. include:: ../README.md
"""

import warnings

try:
    from .compiler import *
    from .builder import *
except ImportError as e:
    warnings.warn(ImportWarning(e))

__version__ = "0.1.1.0.11.0"
__author__ = "nielstron"
__author_email__ = "n.muendler@web.de"
__copyright__ = "Copyright (C) 2023 nielstron"
__license__ = "MIT"
__url__ = "https://github.com/imperatorlang/hebi"
