'''
Ryan Webster
A451
Python Exercise 3
'''

# import modules
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
import pandas as pd

# Reading in pleiades data file
data = pd.read_csv('Pleiades.csv')

# Extracting relevant information.
# Color of the data points will be determined
# by the spectral type
ra = data['RA (2000)']
dec = data['Dec(2000)']
Vmag = data['Vmag']
spec_type = data['SpType']

# Defining maximum and minimum
# marker sizes
max_ms = 5
min_ms = 1

# Creating a linear function to calculate marker size
# from Vmag. Note: size magnitudes are reversed, the slope
# has min - max in the denominator
slope_ms = (max_ms-min_ms)/(np.min(Vmag)-np.max(Vmag))
# y-intercept of linear function
b_ms = max_ms - np.min(Vmag)*slope_ms

# Calculating marker size from Vmag
# Note: 's' in plt.scatter takes as input the intended
# AREA of the point, not the radius.
# To appropriately scale the marker, the linear function
# is squared.
scaled_ms_pd = (slope_ms*Vmag + b_ms)**2

# Creating a dictionary to convert from spectral type to a color in matplotlib
color_dict = {'O':'mediumblue','B':'steelblue','A':'paleturquoise','F':'lightyellow','G':'wheat','K':'orange','M':'orangered','~':'white','D':'steelblue'}

# Looping thru spectral types
plot_colors = []
for star in spec_type:
    # Indexing first letter out of spectral type string
    spec = star[0]
    # This gives me the spectral type (OBAFGKM) of the star
    # I then use the dictionary to get the matplotlib color 
    # and append it to the plot_colors list
    plot_colors.append(color_dict[spec])
    
# Now that I have RA, Dec, markersizes, and colors, I can input 
# everything to matplotlib and get a finding chart
plt.style.use('dark_background')

plt.title('Pleiades Finding Chart', fontsize=14)
plt.scatter(ra,dec,s=scaled_ms_pd,c=plot_colors)
plt.xlabel('R.A')
plt.ylabel('Dec')
plt.savefig('pleiades_finding_chart.png',dpi=300)
plt.show()





