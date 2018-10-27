# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:28:21 2018

@author: shubham and shreya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#Number of sensor nodes deployed
N = 1000      
E = 1        
l = 200
b = 200
h = 10      

#Random distribution of sensor nodes in a volume of l*b*h
x = np.random.uniform(low=0, high=l, size=N)
y = np.random.uniform(low=0, high=b, size=N)
z = np.random.uniform(low=0, high=h, size=N)

#Position of Base Station
bs_x = 100
bs_y = 100
bs_z = 5

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Axis labels set
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.scatter(x,y,z)
ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)

#Sensor nodes with their corresponding energy
pos = np.dstack((x,y,z))
pos_e = {tuple(pos[0][i]):E for i in range(0,N)}      #list(pos_e.keys())[0] : To acces at 0th index

#Distance of each sensor node from base station
dist = ((x-bs_x)**2 + (y-bs_y)**2 + (z-bs_z)**2))**1/2
ener = np.full((1000), E)


