#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" bokeh.py """
# @imports
import json  # requires python >= 2.6
import sys
from typing import Dict

from bokeh.io import output_file, show

from bokeh.plotting import figure

# @info
name = "bokeh"
json_file = sys.path[0] + "/" + name + ".json"

# @functions
