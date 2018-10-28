# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:24:43 2018

@author: lenovo
"""

from threeD_deploy import *
from fuzzy_radius import *

T = 0.3
r_comp = np.full((N), -np.inf)

tent_CH = [] 

for i in range(N):
    alpha = np.random.random()
    if alpha<T:
       radius.input['energy'] = ener[i]
       radius.input['dist_to_base'] = dist[i]
       radius.compute()
       r_comp[i] = radius.output['comp_radius']
       tent_CH.append(i)
       ax.scatter(x[i], y[i], z[i], c='g', marker='.', s=200)

print(len(tent_CH))
       
for i in range(len(tent_CH)):
    indi = tent_CH[i]
    for j in range(len(tent_CH)):
        indj = tent_CH[j]
        if ((x[indj]-x[indi])**2+ (y[indj]-y[indi])**2 + (z[indj]-z[indi])**2)**(1/2) <= r_comp[indi]:
            if ener[indj] > ener[indi]:
                del tent_CH[indj]
                ax.scatter(x[indi], y[indi], z[indi])
                break

print(len(tent_CH))
            
     

       
       
    
