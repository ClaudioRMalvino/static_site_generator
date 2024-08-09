#!/usr/bin/env fish

set -gx PYTHONPATH $PYTHONPATH (pwd)
python3 -m unittest discover -s tests
