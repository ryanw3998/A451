'''
Ryan Webster
A451
Python Exercise 3
'''

import numpy as np
import matplotlib.pyplot as plt

m1 = np.linspace(0.1,1,num=10)
m2 = np.linspace(1,10,num=10)
m3 = np.linspace(10,100,num=10)

m = np.concatenate([m1,m2,m3])
print(m)




