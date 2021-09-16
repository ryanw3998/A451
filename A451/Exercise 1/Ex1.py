'''
Ryan Webster
A451
Key for Python Exercise 1
'''

#This sample program reads star data from the file Ex1.csv
#and plots a color-magnitude diagram.
#
#import the packages needed:
#the numpy package contains Python tools for scientific computing
import numpy as np
#the matplotlib package contains Python tools for plotting
import matplotlib.pyplot as plt
#the pandas package contains data analysis tools
import pandas as pd

'''*****************Part A*****************'''

#read in the Ex1.csv file.
#column headings = Name, LHS, Parallax, SpType, Bmag, Vmag
#"pd.read.csv" tells Python to execute the read.csv tool in the pandas library
starlist = pd.read_csv("Ex1.csv")

#compute the B-V color of each star.
color = starlist['Bmag'] - starlist['Vmag']

#compute the absolute V magnitude of each star.
#remember:  m-M=5log10(distance/10)
#"np.log10" tells Python to execute the log10 function in numpy
absmag = starlist['Vmag'] - 5.0*np.log10(1.0/(starlist['Parallax']*10.))

#plot the B-V color on the x-axis and absolute V magnitude on the y-axis.
#the 'bo' indicates that the points should be plotted with blue circles.
#the "plt" tells Python the commands are in matplotlib
plt.plot(color, absmag, 'bo')

#set the limits on the x- and y-axes.
#note that the y-axis is plotted with larger magnitudes on the bottom.
plt.axis([-0.5,2.5,20,0])

#make sure the tick marks on both axes point inside the plot.
plt.tick_params(which='both', direction='in') 

#label the x and y axes
plt.xlabel('B-V')
plt.ylabel('Absolute V Magnitude')

#save the plot as a pdf file.  Other options include png, ps, eps, and jpg.
plt.savefig('CMD.png')

#produce the plot
plt.show()

'''*****************Part B*****************'''

# Calculatin bolometric correction from:
BC = -2.1*(color)**4 + 6.1*(color)**3 - 6.3*(color)**2 + 2.1*(color) - 0.15

# Applying bolometric correction. Note: BC returns NEGATIVE values, meaning you
# ADD it to the absmag. Remebers, bolometric corrections should always add brightness
# to the star, therefore decreasing the value of the magnitude.
M = absmag + BC

# Calculating luminosity from stars in units of Lsun
L = 10**(-.4*(M-4.83))

# Calculating temperature in units of Kelvin
Temp = -1700*(color)**3 + 6300*(color)**2 - 9100*(color) + 9500

# Plotting luminosity vs temp. Plot is logarithmic for Luminosity
# This is done by using plt.semilogy()
plt.semilogy(Temp,L,'bo')

# This line will invert the x axis without needing to define limits.
# This can also be done for the y axis with plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

# Labeling x and y axis
plt.xlabel('Temp (K)')
plt.ylabel('Luminosity (Lsun)')

# Save figure
plt.savefig('HRD.png')

# Produce plot
plt.show()