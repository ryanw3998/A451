'''
Ryan Webster
A451 Python Exercise 5 Key
'''

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Relevant values
Tsun = 5778.0 # K

# Values provided in problem
mass = 0.5 # Msun
t1 = 10**6 # years
t2 = 10**11 # years
Ti = 10**5 # K
tau0_wd = 700*10**6 # years

# Luminosity-time relation
def lum_func_time(L0,t,tau0):
    return L0*(1+(5*t)/(2*tau0))**(-7/5)

# Calculates white dwarf radius in Rsun
def wd_radius(M):
    return (1/74)*(M)**(-1/3)

# Luminosity equation in Lsun
def luminosity(R,T):
    return (R**2)*(T**4)

# Temperature equation in Tsun
def temperature(L,R):
    return (L/(R**2))**(1/4)

# Log space time array
time_arr = np.logspace(6,11,20)

# Calculating radius of star
radius_star = wd_radius(mass)
# Calculating inital luminosity
L0_star = luminosity(radius_star,Ti/Tsun)
# Calculating lum as function of time
Lvt = lum_func_time(L0_star,time_arr,tau0_wd)
# Calculating temperature as function of time
Tvt = temperature(Lvt,radius_star)

# Creating data frame to save table
table_dict = {'log(Time)':time_arr,'log(L/Lsun)':Lvt,'log(T/Tsun)':Tvt}
table_df = pd.DataFrame(table_dict)
table_df.to_csv('wd_table.csv')

# using tabulate to print readable table to terminal
print(tabulate(table_df,headers='keys',tablefmt='psql',floatfmt=['int','.3e','.3f','.3f']))


