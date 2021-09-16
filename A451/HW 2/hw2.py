'''
Ryan Webster
A451
Written HW 2 Key
'''

# Import modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Defining useful physical constants in MKS units
G = 6.67*10**-11 # grav
k = 1.4*10**-23 # Boltzmann
m = 0.6*(1.6*10**-27) # Mean molecular mass
sigma = 5.67*10**-8 # Stefan-Boltzmann constant
c = 2.99*10**8 # Speed of light

# Defining dictionary of masses and radii
d = {'Mass': [0.1,0.5,1,2,5,10,20,50], 'Radius': [0.15,0.5,1.0,1.7,3.3,6.3,11,23]}
# Converting dictionary to pandas dataframe
data = pd.DataFrame(d)

# Defining volume function
def volume(R):
    return (4/3)*np.pi*R**3

# Defining density function
def density(M,R):
    vol = volume(R)
    return M/vol

# Defining average temperature equation ()
def avg_temperature(M,R):
    return (m*G*M)/(5*k*R)

# Calculate average density. df.mul() multiplies desired data frame by the value in 
# paraenthesis. This allows me to convert Mass to units of kg and Radius to units of
# meters. This is need for calculating density and temperature in MKS units
avg_density = density(data['Mass'].mul(2*10**30),data['Radius'].mul(7*10**8))

# Print values for table
print(avg_density)

# Calculating temperature
avg_temp = avg_temperature(data['Mass'].mul(2*10**30),data['Radius'].mul(7*10**8))

# Print values for table
print(avg_temp)

# Plotting average density vs mass
plt.loglog(data['Mass'],avg_density)

# label axes
plt.xlabel('Mass (Msun)')
plt.ylabel('Average Density (kg m^-3)')

# Save plot
plt.savefig('density_vs_mass.png')

# Generate plot
plt.show()

# Plotting typical internal temperature vs mass
plt.loglog(data['Mass'],avg_temp)

# Label axis
plt.xlabel('Mass (Msun)')
plt.ylabel('Internal Temperature (K)')

# Save plot
plt.savefig('temp_vs_mass.png')

# Generate plot
plt.show()
