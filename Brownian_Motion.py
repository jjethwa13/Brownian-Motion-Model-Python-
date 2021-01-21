# =============================================================================
# Model for implementing a Brownian Motion
# =============================================================================

import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas import Series
import numpy as np

class Brownian_Motion(object):
    
    def __init__(self, dt=0.01):
        
        self.data = Series(data=[0], index=[0], name="Brownian Motion Data")
        self.dt = dt
        self.time = 0
    
    def set_dt(self, dt):
        self.dt = dt
    
    def get_dt(self):
        return self.dt
    
    def get_time(self):
        return self.time
    
    def simulate(self, s):
        
        if s < self.time:
            pass
        else:
            simulation_index = [self.time + n*self.dt for n in range(1, int((s - self.time)/self.dt) + 1)]   ## Creates the Index that we are simulating
            simulation_data = []
            prev_t = self.data.index[-1]
            prev_data = self.data.loc[prev_t]
            for t in simulation_index:
                sd = np.sqrt(t - prev_t)
                simulation_data.append(prev_data + norm.rvs(scale=sd))
                prev_t = t
                prev_data = simulation_data[-1]
            
            
            
            self.data = self.data.append(Series(data=simulation_data, index=simulation_index, name="Brownian Motion Data"))
            self.time = s
        
        return self.data
            

#B = Brownian_Motion()
#data = B.simulate(200)
#
#
#plt.figure(figsize=(20,10))
#plt.title("Brownian Motion")
#plt.xlabel("Time")
#plt.ylabel("Bt")
#plt.grid(True)
#plt.plot(data)
#plt.show()
#
#data = B.simulate(300)
#
#
#plt.figure(figsize=(20,10))
#plt.title("Brownian Motion")
#plt.xlabel("Time")
#plt.ylabel("Bt")
#plt.grid(True)
#plt.plot(data)
#plt.show()
        
