'''
Ryan Webster
A451
Python Homework 2
'''

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading in data
data = pd.read_csv('star-1.csv')

wl = data['Wavelength']
flux = data['Flux']

teff = float(input('Enter Temperature: '))

def planck(Lambda,Temp):
    top = (1.19*10**24)/(Lambda**5)
    bottom = np.exp((1.438*10**8)/(Lambda*Temp))-1
    return top/bottom

def scale_planck(Lambda,Temp):
    planck_5160 = (2.09*10**-12)/planck(5160,Temp)
    return planck(Lambda,Temp)*planck_5160

temp_high = teff+2000
temp_low = teff-2000

fit = scale_planck(wl,teff)
fit_high = scale_planck(wl,temp_high)
fit_low = scale_planck(wl,temp_low)

plt.plot(wl,flux,label='Data',color='k')
plt.plot(wl,fit,label='Teff: {} K'.format(teff))
plt.plot(wl,fit_high,label='Teff: {} K'.format(teff+2000))
plt.plot(wl,fit_low,label='Teff: {} K'.format(teff-2000))
plt.ylabel('Normalized Flux')
plt.xlabel('Wavelength (angs)')
plt.legend()
plt.show()

