'''
Ryan Webster
A451
Python Exercise 3
'''

# Importing modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing double star data
ds_data = pd.read_csv('debs.csv')

# Extracting mass and radius data from columns
star1_mass = ds_data['logm1']
star2_mass = ds_data['logm2']
star1_radius = ds_data['lograd1']
star2_radius = ds_data['lograd2']

# Using np.linespace to generate masses
# Each mass range requires a different linespace, since the 
# spacing is not the same
m1 = np.arange(0.1,1,.1)
m2 = np.arange(1,10,1)
m3 = np.arange(10,110,10)

# Combining all mass arrays into one array
Ms = np.concatenate([m1,m2,m3])
print(Ms)
# Defining empty array for radius values
# This array will be populated as the for loop runs
Rs = np.zeros(len(Ms))

# mass-radius relationship
# In units of Msun and Rsun, the proportionality
# becomes an equation
def mass_radius_rel(M,Beta):
    return M**((Beta-1)/(Beta+3))


# Looping through masses, calculating R.
# 'for' loops begin like so. The general syntax is
# "for 'variable' in 'array'. The solution below uses
# range(len(Ms)) which generates a list of values from 
# 0 to the length of Ms, which is 30. In other words,
# range(len(Ms)) is all integers 0 to 29 in a list. 
# The integers are assigned to 'i' as the loop runs. 
# The loop finishes when it reachs the end of the list
# Note, 'for' loops start at N1 and go up to, but does not include
# N2. In this case, it starts at 0 and goes up to 30. So the final
# number is 29. 
for i in range(0,len(Ms)):
    # By using Ms[i], I can get the ith Ms value
    star_mass = Ms[i]

    # Now, I check what the mass of the star is
    # If its smaller or equal to 1, it uses Beta = 4
    if star_mass <= 1:
        # print(4,star_mass)
        beta_pow = 4

    # If it is larger than 1, it uses Beta = 17
    else:
        # print(17,star_mass)
        beta_pow = 17

    # Once I have the star's mass and Beta, I plug them into
    # my equation for the mass-radius relation. The ith element
    # of the Rs array is then replaced with the value of 
    # the mass_radius_rel function. 
    Rs[i] = mass_radius_rel(star_mass,beta_pow)

# Once i = 29, the script exists the for loop
# Now, I have an array of Ms and Rs. I convert the values
# to log base 10 for the plot.
plt.plot(np.log10(Ms),np.log10(Rs),label='R(M)')

# Plotting double stars from debs.csv
plt.plot(star1_mass,star1_radius,'ko',ms=1,label='Data')
plt.plot(star2_mass,star2_radius,'ko',ms=1)


# Adding labels and legend
plt.xlabel('log Mass (Msun)')
plt.ylabel('log Radius (Rsun)')
plt.legend()

# Save plot
plt.savefig('radius_mass.png')

# Show plot
plt.show()









