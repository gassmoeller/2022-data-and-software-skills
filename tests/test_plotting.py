#!/bin/python

"""This module contains functions to test our plotting script."""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import plotting

def test_plot():
    plotting.plot()

def test_read_data():
    current_file_location = os.path.dirname(__file__)
    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    input_data_filename = os.path.join(data_directory,
                                        "110-tavg-12-12-1950-2020.csv")
    temperature_data = plotting.read_data(input_data_filename)

    assert temperature_data.shape == (71,3), \
        "Unexpected size of array. Array size: " + str(temperature_data.shape)

def test_process_data():
    test_input_data = np.array([[0,32],[1,212]])
    test_output = plotting.process_data(test_input_data)
    test_expected_output = np.array([[0,32,273],[1,212,373]])

    assert np.all(test_output == test_expected_output), \
        "The process_data function returned an unexpected result."

def test_plot_data():
    current_file_location = os.path.dirname(__file__)
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    plot_filename = os.path.join(results_directory,
                                "temperature-over-time.pdf")

    if os.path.exists(plot_filename):
        os.remove(plot_filename)

    test_expected_output = np.array([[0,32,273],[1,212,373]])
    plotting.plot_data(test_expected_output, plot_filename)

    assert os.path.exists(plot_filename)

def test_csv_to_json():
    current_file_location = os.path.dirname(__file__)

    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    conversion_filename = os.path.join(data_directory,
                                        "110-tavg-12-12-1950-2020.csv")
    json_filename = os.path.join(results_directory,
                                        "data_output.json")
    plotting.csv_to_json(conversion_filename, json_filename)

    input_data = pd.read_csv(conversion_filename, index_col='Date', header=4)
    converted_data = pd.read_json(json_filename)
    assert input_data.info() is converted_data.info(), \
        "Error during conversion."