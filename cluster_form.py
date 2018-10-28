# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:47:45 2018

@author: shreya
"""

from threeD_deploy import *
from fuzzy_radius import *
from CH_select  import *

simul_no = 10

cluster_count = dict.fromkeys(tent_CH,1)
cluster = {}

for i in range(N):
    if is_CH[i] == False:
        sd = np.inf
        for j in range(len(tent_CH)):
            ind= tent_CH[j]
            d = ((x[i]-x[ind])**2 +(y[i]-y[ind])**2 + (z[i]-z[ind])**2)**(1/2)
            if d < sd:
                sd = d
                sind = ind
        cluster_count[sind] = cluster_count[sind]+1
        cluster.setdefault(sind,[]).append(i)

for k in range(simul_no):
    for i in range(N):
        if is_CH[i] == True:
            e = ener[i]
            if e > 0:
                dis = ((x[i]-bs_x)**2 + (y[i]-bs_y)**2 + (z[i]-bs_z)**2)**(1/2)
                e = e - (( 51200 * (10 ** (-9))* (cluster_count[i]) ) + ( 102400 * (10 ** (-12)) * (dis ** 2)))
                if e <= 0:
                    d_count = d_count + 1
                else:
                    ener[i] = e
        else:
            e = ener[i]
            if e > 0:
                chf=False
                for CH, node in cluster.items():
                    for n in node:
                        if n == i:
                            CH_x = x[CH]
                            CH_y = y[CH]
                            CH_z = z[CH]
                            chf=True
                            break
                    if chf==True:
                        break
                dis = ((x[i]-CH_x)**2 + (y[i]-CH_y)**2 + (z[i]-CH_z)**2)**(1/2)
                e = e - (( 51200 * (10 ** (-9)) ) + ( 102400 * (10 ** (-12)) * (dis ** 2)))
                if e <= 0:
                    d_count = d_count + 1
                else:
                    ener[i] = e
                
        


         
