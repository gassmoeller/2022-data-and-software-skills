#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data (filename, header_line = 5):
    """ read data.csv """

    # Create an array (a multi-dimensional table) out of our data file, full of text
    text_data = np.genfromtxt(filename, delimiter=',',skip_header=header_line)
    print(text_data)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(text_data[header_line:,:], dtype=float)

    return temperature_data



def process_data(temperature_data):
#   temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv")
# Compute a new column by multiplying column number 1 to Kelvin
    temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273
    processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
    
    return processed_temperature_data



# Append this new column to the existing temperature_data array

# print (processed_temperature_data)

# Create a figure of the processed data

def plot_and_save_figure(processed_temperature_data):

    temperature_figure = plt.figure()
    temperature_plot = plt.bar (processed_temperature_data[:,0],
                            processed_temperature_data[:,2],
                            width=40)
    plt.show(block=True)
    temperature_figure.savefig('results/temperature-over-time.pdf')


temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv")
processed_temperature_data = process_data (temperature_data)

def csv_to_json(filename):

    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json("results/data_output.json")



assert temperature_data.shape == (71,3), \
    'unexpected size of array, array size:' + str(temperature_data.shape)

temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv")
processed_temperature_data = process_data (temperature_data)
plot_and_save_figure(processed_temperature_data)
csv_to_json("data/110-tavg-12-12-1950-2020.csv")


