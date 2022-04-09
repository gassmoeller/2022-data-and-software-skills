#!/bin/python

"""Main tests our plotting script"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import data_script