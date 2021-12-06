'''
Ryan Webster
A451
Script for Python Exercise 6
'''

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in data, extract data, generate range of periods
data = pd.read_csv('51peg.csv')
time = data['Day']
rv = data['RV (m/s)']
periods = np.arange(4.10,4.40,0.03)

# Radial velocity function
def rad_vel(phase):
    return 63*np.sin(2*np.pi*phase)+9

# Loop thru periods
resids_stats = []
for p in periods:

    phases = time/p # calculate phases of data
    rad_v = rad_vel(phases) # estimate radial velocity

    resids = rv-rad_v # subtract estimation from data
    resids_stats.append(np.std(resids)) # calculate standard deviation, append to array

# Lowest residual value
lowest_resid = np.min(resids_stats)
# Corresponding period of lowest residual value
best_per_val = periods[np.where(lowest_resid==resids_stats)][0]

print('Period with best fit to data: {} days'.format(np.round(best_per_val,2)))

# plotting residuals
plt.scatter(periods,resids_stats)
plt.plot(best_per_val,lowest_resid,'ro',ms=7,label='Best Fit')
plt.ylabel(r'$\sigma$ Residuals')
plt.xlabel('Period (Days)')
plt.legend()
plt.savefig('sig_residual.png',dpi=300)
plt.show()
