#!/bin/python

"""This module contains functions to read and plot temperature data."""

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename, header_lines=5):
    """Read data from a .csv data file named 'filename', skipping
    the first 'header_lines' lines. Return the data as a Numpy array."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    text_data = np.genfromtxt(filename, delimiter=',',skip_header=header_lines)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    data = np.array(text_data[:,:], dtype=float)
    return data

def process_data(temperature_in_fahrenheit):
    """Convert temperature array in degree Fahrenheit to degree Kelvin
    and append to the input data array."""
    # Compute a new column by multiplying column number 1 to Kelvin
    temperature_kelvin = (temperature_in_fahrenheit[:,1,None] - 32) * 5/9 + 273

    # Append this new column to the existing temperature_data array
    combined_temperature_data = np.append(temperature_in_fahrenheit, temperature_kelvin,1)
    return combined_temperature_data

def plot_data(combined_temperature_data):
    """Create a figure of the processed data"""
    figure = plt.figure()
    plt.bar (combined_temperature_data[:,0],
                                combined_temperature_data[:,2],
                                width=40)
    plt.show(block=True)
    figure.savefig('results/temperature-over-time.pdf')

def csv_to_json(filename):
    """Convert a csv file named 'filename' to json."""
    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json("results/data_output.json")
    print("Some values of our data:", all_data.loc['195012':'197512','Value'])

def plot():
    """Main plotting function."""
    temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv")

    assert temperature_data.shape == (71,3), \
        "Unexpected size of array. Array size: " + str(temperature_data.shape)

    processed_temperature_data = process_data(temperature_data)

    test_input_data = np.array([[0,32],[1,212]])
    test_output = process_data(test_input_data)
    test_expected_output = np.array([[0,32,273],[1,212,373]])

    assert np.all(test_output == test_expected_output), \
        "The process_data function returned an unexpected result."

    if os.path.exists('results/temperature-over-time.pdf'):
        os.remove('results/temperature-over-time.pdf')

    plot_data(processed_temperature_data)

    assert os.path.exists('results/temperature-over-time.pdf')

    conversion_filename = "data/110-tavg-12-12-1950-2020.csv"
    json_filename = "results/data_output.json"
    csv_to_json(conversion_filename)

    input_data = pd.read_csv(conversion_filename, index_col='Date', header=4)
    converted_data = pd.read_json(json_filename)
    assert input_data.info() is converted_data.info(), \
        "Error during conversion."
