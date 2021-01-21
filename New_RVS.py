# =============================================================================
# Creating new Random Stochastic Processes with the Brownian Motion Model
# =============================================================================

import Brownian_Motion as bm
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt

def RV(func, t, dt=0.1):
    
    B = bm.Brownian_Motion(dt=dt)
    brownian_data = B.simulate(t)
    result_t = brownian_data.index
    result_data, result_name = func(result_t, brownian_data)
    
    return Series(data=result_data, index=result_t, name=result_name)

        
def Geometric(t, Bt):
    
    x = 1
    mu = 0.2
    sig = 1
    
    return x*np.exp((mu - ((sig**2)/2))*t + sig*Bt), "Geometric Brownian Motion"

def Brownian_Bridge(t, Bt):
    
    ## Note must have t >= 1 or else B1 won't be defined
    ## Typically t is defined on [0,1] so this must be specified
    
    return Bt - t*Bt.loc[1], "Brownian Bridge"

def Sin_Brownian(t, Bt):
    
    return np.sin(Bt), "Sinusoidal Brownian Motion"

def Sinh_Brownian(t, Bt):
    
    return np.sinh(Bt), "Hyperbolic (Sinh) Brownian Motion"

data = RV(Sinh_Brownian, 10, dt=0.001)


plt.figure(figsize=(20,10))
plt.title(data.name)
plt.xlabel("Time")
plt.ylabel("Xt")
plt.grid(True)
plt.plot(data)
plt.show()
    