#!/bin/python

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

all_data = np.genfromtxt("/Users/ashleyd/Desktop/2022-data/returned_assignments/dann_a7/data/temperature_data.csv", delimiter=',',skip_header=0)

temperature_data = np.array(all_data[0:,0:2], dtype=float)

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

temperature_figure.savefig('./temperature-over-time.pdf')

# reads the .csv file so it could be put into the .json file
all_data = pd.read_csv("/Users/ashleyd/Desktop/2022-data/returned_assignments/dann_a7/data/final_processed_temps.csv", index_col='Date', header=0)
all_data.info()
all_data.to_json("data_output.json")

print(all_data.loc['194812':'202012','Temperature (K)'])

json_data = pd.read_json("data_output.json")
json_data.info()

print(json_data.loc['194812':'202012','Temperature (K)'])

temperature_plot = plt.plot (processed_temperature_data[:,0],processed_temperature_data[:,2])
plt.show(block=True)