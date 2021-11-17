'''
Ryan Webster
Script for written homework #5
Problem 2
'''


'''
Note: I converted the xlsx file to a csv
for better compatability with pandas
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data
data = pd.read_csv('HW5_Data.csv')

# Extract column information
date = data['HJD-2450000']
mag = data['mag']
error = data['error']

# Plot
plt.scatter(date,mag,s=2)
plt.xlabel('HJD-2450000')
plt.ylabel('Mag')
plt.show()

# These values were found by eye
# on the plot
n_peaks = 11
date1 = 2106
date2 = 2225

# Calculating period
period = np.round((date2-date1)/n_peaks,2)
print(period)

# Getting phase for all data points
phase = ((date-date1)/period) % 1
print(phase)

# Plotting
plt.scatter(phase,mag,s=2)
plt.xlabel('Phase')
plt.ylabel('Mag')
plt.show()
