#!/bin/bash
python nml_patcher.py -f "JPplusShinkansen.pnml" -o "JPplusShinkansen.nml" -b 1 -v 1
nmlc JPplusShinkansen.nml -o JPplusShinkansen.grf -c -t src/custom_tags.txt -l src/lang
python move_grf.py