#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

all_data = np.genfromtxt("original-temperature-data.csv", delimiter=',',skip_header=0)

print(all_data)

temperature_data = np.array(all_data[0:,0:2], dtype=float)


temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

original_temperature_data = np.append(temperature_data, temperature_kelvin,1)
print (original_temperature_data)

temperature_figure = plt.figure()
temperature_plot = plt.plot (original_temperature_data[:,0],original_temperature_data[:,2])
plt.show(block=True)

# adds labels to plot
plt.title("Maximum Annual Temperature in Miami, Florida")
plt.xlabel ('Date')
plt.ylabel ('Temperature (K)')

temperature_figure.savefig('./temperature-over-time.pdf')

# reads the .csv file so it could be put into the .json file
all_data = pd.read_csv("final_processed_temps.csv", index_col='Date', header=0)
all_data.info()
all_data.to_json("data_output.json")

print(all_data.loc['194812':'202012','Temperature (K)'])

json_data = pd.read_json("data_output.json")
json_data.info()

print(json_data.loc['194812':'202012','Temperature (K)'])

temperature_plot = plt.plot (original_temperature_data[:,0],original_temperature_data[:,2])
plt.show(block=True)