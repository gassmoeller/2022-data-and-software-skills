#!/bin/python

"""Tests our plotting script"""

import sys
import os
import numpy as np

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import data_script

def test_csv_to_json():
    """Tests the csv_to_json function"""
    current_file_location = os.path.dirname(__file__)

    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    conversion_filename = os.path.join(data_directory,
                                        "temperature_data.csv")
    json_filename = os.path.join(results_directory,
                                        "data_output.json")
    data_script.csv_to_json(conversion_filename, json_filename)

def test_process_data():
    """Tests the process_data function"""
    test_input_data = np.array([[0,32],[1,212]])
    test_output = data_script.process_data(test_input_data)
    test_expected_output = np.array([[0,32,273],[1,212,373]])

def test_plot_data():
    """Tests the plot_data function"""
    current_file_location = os.path.dirname(__file__)
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    plot_filename = os.path.join(results_directory,
                                        "temperature-over-time.pdf")

    if os.path.exists(plot_filename):
        os.remove(plot_filename)

    test_expected_output = np.array([[0,32,273],[1,212,373]])
    data_script.plot_data(test_expected_output, plot_filename)
