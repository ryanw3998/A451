'''
Ryan Webster
A451
Script to calculate reaction rates for HW 3
'''

import numpy as np

k = 1.38*10**-23
u = 1.66*10**-27
c = 2.99*10**8
Xa = 0.5
alpha = 1/137

def Egfunc(Za,Zb,ma,mb):
    mr = (ma*mb)/(ma+mb)
    return 2*((np.pi*alpha*Za*Zb)**2)*mr*(c**2)

def reactionAB(Aa,Ab,rho,Za,Zb,Eg,SEo,T):
    p1 = ((6.48*10**-24)*(Aa+Ab)*Xa*rho**2)/(Za*Zb*(Aa*Ab*u)**2)
    p2 = SEo*(Eg/(4*k*T))**(2/3)
    p3 = np.exp(-3*(Eg/(4*k*T))**(1/3))

    return p1*p2*p3

# def iso_ratio():
    # return ()

# For each reaction
Aa_arr = [1,1,1,1]
Ab_arr = [12,13,14,15]
ma_arr = [1*u,1*u,1*u,1*u]
mb_arr = [12*u,13*u,14*u,15*u]
Za_arr = [1,1,1,1]
Zb_arr = [6,6,7,7]
rec_names = ['P-12C','P-13C','P-14N','P-15N']

# For each star mass
mass_arr = [1,2,5,10]
SEo_arr = [1.5,5.5,3.3,78]
rho_arr = [10**5.1,10**4.8,10**4.3,10**3.9]
T_arr = [10**7.2,10**7.4,10**7.4,10**7.5]

for i in range(4):
    M = mass_arr[i]
    rhoc = rho_arr[i]
    T = T_arr[i]
    print('Mass: ',M)
    for j in range(4):
        print(rec_names[j])
        Za = Za_arr[j]
        Zb = Zb_arr[j]
        ma = ma_arr[j]
        mb = mb_arr[j]
        Aa = Aa_arr[j]
        Ab = Ab_arr[j] 
        SEo = SEo_arr[j]
        Egcalc = Egfunc(Za,Zb,ma,mb)
        RXrec = reactionAB(Aa,Ab,rhoc,Za,Zb,Egcalc,SEo,T)

        print(RXrec)
    print()

