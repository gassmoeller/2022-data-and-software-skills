#!/bin/python

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename, header_lines=0):
    """Read data from a .csv data filed named 'filename', skipping
    the first 'header_lines'. Return the data as a Numpy array so it could be read as numbers."""
   
    text_data = np.genfromtxt(filename, delimiter=',',skip_header=header_lines)

    data = np.array(text_data[0:,0:2], dtype=float)
    return data

def process_data(temperature_in_fahrenheit):
    '''Convert temperature array in degree Farenheit to
    degree Kelvin and append to the input data array so all the data is together.'''
    
    temperature_kelvin = (temperature_in_fahrenheit[:,1,None] - 32) * 5/9 + 273

    combined_temperature_data = np.append(temperature_in_fahrenheit, temperature_kelvin,1)
    return combined_temperature_data

def plot_data(combined_temperature_data, plot_filename):
    """Figure for new processed data"""
    figure = plt.figure()
    plt.plot (combined_temperature_data[:,0],
                    combined_temperature_data[:,2])
    plt.show(block=True)
    figure.savefig(plot_filename)

temperature_data = read_data("data/temperature_data.csv")
processed_temperature_data = process_data(temperature_data)

def csv_to_json(filename, output_filename):
    """Convert a csv file named 'filename' to json"""
    all_data = pd.read_csv(filename, index_col='Date', header=0)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    """Plotting function"""
    current_file_location = os.path.dirname(__file__)

    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")

    input_data_filename = os.path.join(data_directory,
                                        "temperature_data.csv")

    temperature_data = read_data(input_data_filename)

    processed_temeprature_data = process_data(temperature_data)

    plot_filename = os.path.join(results_directory,
                                        "temperature-over-time.pdf")

    plot_data(processed_temperature_data, plot_filename)

    conversion_filename = os.path.join(data_directory,
                                        "temperature_data.csv")
    json_filename = os.path.join(results_directory,
                                        "data_output.json")
    csv_to_json(conversion_filename, json_filename)

temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
print (processed_temperature_data)

temperature_figure = plt.figure()
temperature_plot = plt.plot (processed_temperature_data[:,0],processed_temperature_data[:,2])
plt.show(block=True)

# adds labels to plot
plt.title("Maximum Annual Temperature in Miami, Florida")
plt.xlabel ('Date')
plt.ylabel ('Temperature (K)')

temperature_plot = plt.plot (processed_temperature_data[:,0],processed_temperature_data[:,2])
plt.show(block=True)

if __name__ == "__main__":
    plot()