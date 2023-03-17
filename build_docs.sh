#! /bin/bash
set -e

pip install pdoc3
rm -r docs/hebi
pdoc --html hebi -o docs
