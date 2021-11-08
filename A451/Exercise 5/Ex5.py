'''
Ryan Webster
A451 Python Exercise 5 Key
'''

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

time_arr = np.logspace(6,11,20)

radius_star = wd_radius(mass)
print(radius_star)
L0_star = luminosity(radius_star,Ti/Tsun)
print(L0_star)
Lvt = lum_func_time(L0_star,time_arr,tau0_wd)
print(Lvt)
Tvt = temperature(Lvt,radius_star)
print(Tvt)

table_dict = {'log(Time)':time_arr,'log(L/Lsun)':Lvt,'log(T/Tsun)':Tvt}
table_df = pd.DataFrame(table_dict)
table_df.to_csv('wd_table.csv')

plt.loglog(time_arr,Lvt,label='0.5 Msun White Dwarf')
plt.ylabel('log(L/Lsun)')
plt.xlabel('log(t) (years)')
plt.show()


plt.loglog(time_arr,Tvt*Tsun,label='0.5 Msun White Dwarf')
plt.ylabel('log(T/Tsun)')
plt.xlabel('log(t) (years)')
plt.show()
