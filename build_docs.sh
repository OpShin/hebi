#! /bin/bash
pip install handsdown
handsdown --external `git config --get remote.origin.url` -n hebi --branch master --create-configs --exclude venv

