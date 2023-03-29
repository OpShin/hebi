#! /bin/bash
set -e

pip install pdoc3
rm -r docs/hebi || echo "docs/hebi was missing, that's ok"
pdoc --html hebi -o docs --template-dir docs
