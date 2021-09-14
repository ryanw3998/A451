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

#tell python to make a plot
# plt.ion()

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
# plt.savefig('CMD.png')

#produce the plot
plt.show()

BC = -2.1*(color)**4 + 6.1*(color)**3 - 6.3*(color)**2 + 2.1*(color) - 0.15

M = absmag + BC

L = 10**(-.4*(M-4.74))

print(L)

Temp = -1700*(color)**3 + 6300*(color)**2 - 9100*(color) + 9500

print(Temp)

plt.semilogy(Temp,L,'o')
plt.gca().invert_xaxis()
plt.savefig('HR2.png')
plt.show()