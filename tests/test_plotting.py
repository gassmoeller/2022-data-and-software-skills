#!/bin/python

""" test the plotting script"""
import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__), ".."))

from src import plotting


def test_plot():
    plotting.plot()

def test_read_data():
    current_file_location = os.path.dirname(__file__)
    data_directory = os.path.join(current_file_location, 
                                    "..", 
                                    "data")

    result_directory = os.path.join(current_file_location, 
                                    "..", 
                                    "result")

    input_data_filename = os.path.join(data_directory,
                                    "110-tavg-12-12-1950-2020.csv")

    temperature_data = plotting.read_data(input_data_filename)

    assert temperature_data.shape == (71,3), \
        'unexpected size of array, array size:' + str(temperature_data.shape)


def test_process_data():
    test_input_data = np.array([[0,32],[1,212]]) #first row 0 32, second row 1 212
    test_output = plotting.process_data(test_input_data)
    test_expected_output = np.array([[0,32,273],[1,212,373]])

    assert np.all(test_output == test_expected_output), \
        "The process data function return an unexpeced result"
        

def test_csv_to_json():
    current_file_location = os.path.dirname(__file__)
    data_directory = os.path.join(current_file_location, 
                                    "..", 
                                    "data")

    result_directory = os.path.join(current_file_location, 
                                    "..", 
                                    "result")

    input_data_filename = os.path.join(data_directory,
                                    "110-tavg-12-12-1950-2020.csv")

    
    plotting.csv_to_json(input_data_filename)
    json_file = "results/data_output.json"
    input_data = pd.read_csv(input_data_filename, index_col="Date",header = 4)
    converted_data = pd.read_json(json_file)
    assert input_data.info() is converted_data.info(), \
        "Error during conversion"
