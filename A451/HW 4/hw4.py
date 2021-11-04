'''
Ryan Webster
Script for written HW 4
A451
'''
# Importing relevant modules
import numpy as np
import pandas as pd

'''
PROBLEM 1
'''

# Define array for star masses. I looked up
# these masses online
star_masses = np.array([100,11,2,0.1])

# Funtion for converting mass to lifetime in Gyr
def lifetime(mass):
    return (mass**-2.5)

# Calculating lifetimes
lifetimes = lifetime(star_masses)*10**10
print(lifetimes)
 

'''
PROBLEM 2
'''

# Reading in data, I first had to open it in excel and 
# then save it as a .csv since .xlsx wasn't playing well with
# VS code
star_data = pd.read_csv('Model7M.csv')

# Define useful physical constants
k = 1.38*10**-23 
u = 1.661*10**-27
gamma = 5/3
criteria = (gamma - 1)/gamma

# Define fractional abundances
X = 0.72
Y = 0.25
Z = 0.0

# un-logging rho and T
log_dens = star_data['log rho']
dens = 10**log_dens # kg/m3

log_T = star_data['log T']
temp = 10**log_T # K

# Defining mu and m
mu = (0.72+.25*4)/(0.75+0.25+0.75*1+0.25*2)
# mu = .6
m = mu*u

# Defining Equation 1.11
def ideal_gas_law(rho,T,m_bar):
    pressure = (rho*k*T)/m_bar
    return pressure

# Calculating pressure
pressures = ideal_gas_law(dens,temp,m)
print(pressures)

# Calculating natural log of temp and pressure
ln_T = np.log(temp)
ln_P = np.log(pressures)

# Calculating stability criteria
for i in range(13):
    T1 = ln_T.iloc[i]
    P1 = ln_P.iloc[i]

    T2 = ln_T.iloc[i+1]
    P2 = ln_P.iloc[i+1]

    derv = (T2-T1)/(P2-P1) 

    if derv > criteria:
        print('Convection')
    else:
        print('No convection')


'''
Problem 3
'''

# Temp at r/R = 0.1
T_star = 10**7.41 # K
# Sun core temp
T_sun = 16*10**6 # K

E_pp = (T_star/T_sun)**4
E_cno = (T_star/T_sun)**17.6

percent_pp = 100*.85*E_pp/(.85*E_pp+.15*E_cno)
percent_cno = 100*.15*E_cno/(.85*E_pp+.15*E_cno)

print(np.round(percent_pp,4),np.round(percent_cno,4))
