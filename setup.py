#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

import hebi

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hebi",
    version=hebi.__version__,
    description="A simple pythonic programming language for Smart Contracts on Cardano ",
    author=hebi.__author__,
    author_email=hebi.__author_email__,
    url=hebi.__url__,
    py_modules=["hebi"],
    packages=find_packages(),
    install_requires=[
        "uplc==0.5.6",
        "pluthon==0.2.15",
        "pycardano==0.7.2",
        "frozenlist==1.3.3",
        "pyaiken==0.4.0",
    ],
    tests_require=[
        "hypothesis==6.62.0",
        "parameterized==0.8.1",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=hebi.__license__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.8",
    ],
    keywords="python cardano smart contract blockchain verification haskell",
    python_requires=">=3.8, <3.9",
    test_suite="hebi.tests",
    entry_points={
        "console_scripts": ["hebi=hebi.__main__:main"],
    },
)
