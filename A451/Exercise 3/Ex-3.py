'''
Ryan Webster
A451
Python Exercise 3
'''

# importing modules
import numpy as np
import matplotlib.pyplot as plt

# Using np.linespace to generate masses
# Each mass range requires a different linespace, since the 
# spacing is not the same
m1 = np.linspace(0.1,1,num=10)
m2 = np.linspace(1,10,num=10)
m3 = np.linspace(10,100,num=10)

# Combining all mass arrays into one array
m = np.concatenate([m1,m2,m3])




