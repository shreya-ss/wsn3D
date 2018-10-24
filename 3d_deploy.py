# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:28:21 2018

@author: shreya
"""

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)
N = 1000
x = np.random.uniform(low=0, high=201, size=N)
y = np.random.uniform(low=0, high=201, size=N)
z = np.random.uniform(low=0, high=201, size=N)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.scatter(x,y,z)

