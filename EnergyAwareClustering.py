
#function for Energy Aware Clustering

#Input : x= X_cordinates, y=Y_cordinates, z= Z_cordinates, N= Number of nodes, ener=Energies of nodes

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fuzzy_radius import *
from random import *
N = 200     
E = 1        
l = 200
b = 200
h = 10  
bs_x = 100
bs_y = 100
bs_z = 5    

#Random distribution of sensor nodes in a volume of l*b*h
x = np.random.uniform(low=0, high=l, size=N)
y = np.random.uniform(low=0, high=b, size=N)
z = np.random.uniform(low=0, high=h, size=N)
ener=np.random.uniform(low=0, high=1.0, size=N)

def Energy_Aware_Clustering(x,y,z,N,ener):
    percentage_var=0.3
    tentative_CH=[]
    for x1 in range(0,N):
        prob=random()
        if(prob<percentage_var):
            tentative_CH.append(x1)
    x_dup=[]
    y_dup=[]
    z_dup=[]
    comp_rad=[]
    for x1 in range(0,len(tentative_CH)):
        dist = (float)((x[tentative_CH[x1]]-bs_x)**2 + (y[tentative_CH[x1]]-bs_y)**2 + (z[tentative_CH[x1]]-bs_z)**2)**(1/2)
        radius.input['energy']=1.0
        radius.input['dist_to_base']=dist
        radius.compute()
        comp_rad.append(radius.output['comp_radius'])
    #ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=100)
    #print((final_CH))
#for x1 in range(0,len(tentative_CH)):
 #   print('[ {0} {1} {2} {3} {4} ]'.format(tentative_CH[x1],x[tentative_CH[x1]], y[tentative_CH[x1]],z[tentative_CH[x1]],comp_rad[x1]))
    for x1 in range(0,len(tentative_CH)):
        for y1 in range (0,len(tentative_CH)):
            if((x1!=y1) and (tentative_CH[x1] !=-1)):
                dist_2=((x[tentative_CH[x1]]-x[tentative_CH[y1]])**2 + (y[tentative_CH[x1]]-y[tentative_CH[y1]])**2 + (z[tentative_CH[x1]]-z[tentative_CH[y1]])**2)**(1/2)
                if((comp_rad[x1]>=dist_2) and (comp_rad[y1]>=dist_2)):
                    if(ener[tentative_CH[y1]]>ener[tentative_CH[x1]]):
                        #print(' y= {0} {1} {2}, x= {3} {4} {5} {6} '.format(tentative_CH[y1],ener[tentative_CH[y1]],comp_rad[y1],tentative_CH[x1],ener[tentative_CH[x1]],comp_rad[x1],dist_2))
                        tentative_CH[x1]=-1
                        break
    len1=len(tentative_CH)
    final_CH=[]
    for x1 in range(0,len1):
        if(tentative_CH[x1]!=-1):
            final_CH.append(tentative_CH[x1])
            x_dup.append(x[tentative_CH[x1]])
            y_dup.append(y[tentative_CH[x1]])
            z_dup.append(z[tentative_CH[x1]])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
#Axis labels set
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
    ax.scatter(x,y,z)
    ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=100)
    
Energy_Aware_Clustering(x,y,z,N,ener)