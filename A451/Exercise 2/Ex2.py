'''
Ryan Webster
A451
Python Exercise 2 Key
'''

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading in data
data = pd.read_csv('star-1.csv')

# Extracting wavelength and flux data from star-1.csv
wl = data['Wavelength']
flux = data['Flux']

# Getting temperature from user input 
teff = float(input('Enter Temperature: '))

# Defining planck function
def planck(Lambda,Temp):
    '''
    Planck function as defined in Python Exercise 2 handout
    Input:
    Lambda - wavelength or list of wavelengths
    Temp - temperature to evaluate planck function at

    Output:
    Planck function evaluated at desired wavelength and temperature
    '''
    top = (1.19*10**24)/(Lambda**5)
    bottom = np.exp((1.438*10**8)/(Lambda*Temp))-1
    return top/bottom


# Defining scaling function for planck function. This is necessary for 
# the planck functions to overlap at 5160 angs
def scale_planck(Lambda,Temp):
    '''
    Scales planck function to 5160 Angs
    Input:
    Lambda - wavelength or list of wavelengths
    Temp - temperature to evaluate planck function at

    Output:
    Planck function scaled to 5160 Angs
    '''
    # 2.09*10**-12 comes from star-1.csv file. I simply found the flux
    # value correspnding to 5160 Angs.
    planck_5160 = (2.09*10**-12)/planck(5160,Temp)
    return planck(Lambda,Temp)*planck_5160

# Temperatures 2000 K above and below teff
temp_high = teff+2000
temp_low = teff-2000

# scaled planck functions at teff, temp_high and temp_low
fit = scale_planck(wl,teff)
fit_high = scale_planck(wl,temp_high)
fit_low = scale_planck(wl,temp_low)


# Plotting scaled planck functions and spectrum on same plot
# Spectrum is in black. Fit is in blue, fit high is in orange,
# fit low is in green. Labels are added to each line for the legend
# I used label='Teff: {} K'.format(teff), which allows one to input 
# variables (teff) into strings.
plt.plot(wl,flux,label='Data',color='k')
plt.plot(wl,fit,label='Teff: {} K'.format(teff),color='b')
plt.plot(wl,fit_high,label='Teff: {} K'.format(teff+2000),color='orange')
plt.plot(wl,fit_low,label='Teff: {} K'.format(teff-2000),color='g')

# Axis labels
plt.ylabel('Normalized Flux')
plt.xlabel('Wavelength (angs)')

# Plot legend
plt.legend()

# Save figure
plt.savefig('spectrum_fit.png')

# Show figure
plt.show()

