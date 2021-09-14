import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

G = 6.67*10**-11
k = 1.4*10**-23
m = 0.6*(1.6*10**-27)
sigma = 5.67*10**-8
c = 2.99*10**8

d = {'Mass': [0.1,0.5,1,2,5,10,20,50], 'Radius': [0.15,0.5,1.0,1.7,3.3,6.3,11,23]}
data = pd.DataFrame(d)

def volume(R):
    return (4/3)*np.pi*R**3

def density(M,R):
    vol = volume(R)
    return M/vol

def avg_temp(M,R):
    return (m*G*M)/(5*k*R)

def total_pressure(T,rho):
    Pgas = (rho*k*T)/m 
    Prad = (4*sigma*T**4)/(3*c)
    return Pgas+Prad

avg_density = density(data['Mass'].mul(2*10**30),data['Radius'].mul(7*10**8))
print(avg_density)

avg_temp = avg_temp(data['Mass'].mul(2*10**30),data['Radius'].mul(7*10**8))
print(avg_temp)

pressure = total_pressure(avg_temp,avg_density)
print(pressure)
