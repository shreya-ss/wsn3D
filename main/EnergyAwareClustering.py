
#function for Energy Aware Clustering

#Input : x= X_cordinates, y=Y_cordinates, z= Z_cordinates, N= Number of nodes, ener=Energies of nodes

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fuzzy_radius import *
from random import *
from Show_Graph import *

def Energy_Aware_Clustering(x,y,z,N,ener):
    bs_x = 100
    bs_y = 100
    bs_z = 5
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
    
    for x1 in range(0,len(tentative_CH)):
        for y1 in range (0,len(tentative_CH)):
            if((x1!=y1) and (tentative_CH[x1] !=-1) and (tentative_CH[y1]!=-1)):
                dist_2=((x[tentative_CH[x1]]-x[tentative_CH[y1]])**2 + (y[tentative_CH[x1]]-y[tentative_CH[y1]])**2 + (z[tentative_CH[x1]]-z[tentative_CH[y1]])**2)**(1/2)
                if((comp_rad[x1]>=dist_2)):
                    if(ener[tentative_CH[y1]]>ener[tentative_CH[x1]]):
                        #print(' y= {0} {1} {2}, x= {3} {4} {5} {6} '.format(tentative_CH[y1],ener[tentative_CH[y1]],comp_rad[y1],tentative_CH[x1],ener[tentative_CH[x1]],comp_rad[x1],dist_2))
                        tentative_CH[x1]=-1
                        break
    len1=len(tentative_CH)
    final_CH=[]
    final_comp_r=[]
    for x1 in range(0,len1):
        if(tentative_CH[x1]!=-1):
            final_CH.append(tentative_CH[x1])
            x_dup.append(x[tentative_CH[x1]])
            y_dup.append(y[tentative_CH[x1]])
            z_dup.append(z[tentative_CH[x1]])
            final_comp_r.append(comp_rad[x1])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.suptitle(' Fig 3. Cluster Heads in Energy Aware Clustering',fontsize=20,color='c')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
    ax.scatter(x,y,z,c='b')
    ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=150)
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    show(ax,x_dup,y_dup,z_dup,final_comp_r)
    fig.suptitle(' Fig 4 Spherical Volume of Cluster Heads in Energy Aware Clustering',fontsize=20,color='c')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    for xx in range(0,3):
        ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
        ax.scatter(x,y,z,c='b')
        ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=150)
    
    '''fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.suptitle(' Fig 4.2. Another View of Spherical Volume ofCluster Heads in Energy Aware Clustering',fontsize=20,color='c')
    ax.set_xlim([0,220])
    ax.set_ylim([0,220])
    ax.set_zlim([0,12])
    show(ax,x_dup,y_dup,z_dup,final_comp_r)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    for xx in range(0,3):
        ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
        ax.scatter(x,y,z,c='b')
        ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=150)'''
    
    
