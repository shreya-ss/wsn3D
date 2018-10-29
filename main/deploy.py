import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fuzzy_radius import *
from random import *

#Number of sensor nodes deployed
N = 200     
E = 1.0        
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
fig.suptitle(' Fig 1. Random Deployment of Sensor Nodes',fontsize=20,color='c')
ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500,label='Deploy')
ax.scatter(x,y,z,c='b',label='Deploy')


#Sensor nodes with their corresponding energy
pos = np.dstack((x,y,z))
pos_e = {tuple(pos[0][i]):E for i in range(0,N)}      #list(pos_e.keys())[0] : To acces at 0th index
#print(pos[0][0])
#Distance of each sensor node from base station

ener = np.full((N), E)
is_CH=[False]*N
percentage_var=0.3
in_tentative_CH=[]
for x1 in range(0,N):
    prob=random()
    if(prob<percentage_var):
        in_tentative_CH.append(x1)
x_dup=[]
y_dup=[]
z_dup=[]
comp_rad=[]
in_tentative_len=len(in_tentative_CH)
for x1 in range(0,len(in_tentative_CH)):
    dist = (float)((x[in_tentative_CH[x1]]-bs_x)**2 + (y[in_tentative_CH[x1]]-bs_y)**2 + (z[in_tentative_CH[x1]]-bs_z)**2)**(1/2)
    radius.input['energy']=1.0
    radius.input['dist_to_base']=dist
    radius.compute()
    comp_rad.append(radius.output['comp_radius'])
for x1 in range(0,len(in_tentative_CH)):
        for y1 in range (0,len(in_tentative_CH)):
            if((x1!=y1) and (in_tentative_CH[x1] !=-1) and (in_tentative_CH[y1]!=-1)):
                dist_2=((x[in_tentative_CH[x1]]-x[in_tentative_CH[y1]])**2 + (y[in_tentative_CH[x1]]-y[in_tentative_CH[y1]])**2 + (z[in_tentative_CH[x1]]-z[in_tentative_CH[y1]])**2)**(1/2)
                if((comp_rad[x1]>=dist_2)):
                    if(in_tentative_CH[x1]>in_tentative_CH[y1]):
                        in_tentative_CH[y1]=-1
                        break
in_final_CH=[]
cnt=0
for x1 in range(0,len(in_tentative_CH)):
    if(in_tentative_CH[x1]!=-1):
        in_final_CH.append(in_tentative_CH[x1])
        is_CH[in_tentative_CH[x1]]=True
        x_dup.append(x[in_tentative_CH[x1]])
        y_dup.append(y[in_tentative_CH[x1]])
        z_dup.append(z[in_tentative_CH[x1]])
        
