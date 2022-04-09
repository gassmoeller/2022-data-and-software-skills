#!/bin/python

"""Tests our plotting script"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import data_script

def test_plot():
    data_script.plot()
