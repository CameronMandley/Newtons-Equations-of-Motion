#!/usr/bin/env python
# coding: utf-8

# # Project 01: Newton's Equations of Motion
# 
#    A physical dynamical system consiting of one point mass moving in one dimension at any arbitrary time interval given it's initial state.
#    
#    1. The potential energy of the system is given by:
#    $$U(q) = 2q$$
#    where *q* is the position.
#    
#    2. The system can be described by the following scleronomic, conservative Hamiltonian:
#    $$H(q, p) = U(q) + K(p)$$

# In[36]:


import matplotlib.pyplot as plt
import pandas as pd


# In[37]:


def Newton_Motion(initial_state, mass, tf):
    """
    Takes as an input an initial state X(0) and an arbitrary time instant, t, 
    and outputs the state of the system at time t, X(t).
    """
    
    q0, p0 = initial_state[0], initial_state[1]
    qc, pc = q0, p0
    Hc = 2*qc + ((pc*pc)/mass)*.5

    for ti in range(tf):
        F = -2
        pc += F*ti
        v = pc/mass
        qc += v*ti
        Hc = 2*qc + ((pc*pc)/mass)*.5
        
    return [qc, pc, Hc]


# In[45]:


positions = []
momentums = []

for i in range(5000):
    
    state = Newton_Motion([1.34, 2.5], 3, i)
    positions.append(state[0])
    momentums.append(state[1])
    print("Time: " + str(i))
    print("Position = " + str(state[0]))
    print("Momentum = " + str(state[1]))
    print("Energy = " + str(state[2]))
    print()
    
plt.plot(positions, momentums)
plt.xlabel("positions")
plt.ylabel("momentums")
plt.title("Phase Space Trajectory")
plt.show()
    


# In[ ]:




