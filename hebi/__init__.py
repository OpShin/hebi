#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. include:: ../README.md
"""

import warnings

__version__ = "0.2.0.0.12.5"
__author__ = "nielstron"
__author_email__ = "n.muendler@web.de"
__copyright__ = "Copyright (C) 2023 nielstron"
__license__ = "MIT"
__url__ = "https://github.com/imperatorlang/hebi"

try:
    from .compiler import *
    from .builder import *
except ImportError as e:
    warnings.warn(ImportWarning(e))
