
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fuzzy_radius import *
from random import *

#Number of sensor nodes deployed
N = 200     
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
ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
ax.scatter(x,y,z)


#Sensor nodes with their corresponding energy
pos = np.dstack((x,y,z))
pos_e = {tuple(pos[0][i]):E for i in range(0,N)}      #list(pos_e.keys())[0] : To acces at 0th index
#print(pos[0][0])
#Distance of each sensor node from base station

ener = np.full((1000), E)
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
    x_dup.append(x[tentative_CH[x1]])
    y_dup.append(y[tentative_CH[x1]])
    z_dup.append(z[tentative_CH[x1]])
    dist = (float)((x[tentative_CH[x1]]-bs_x)**2 + (y[tentative_CH[x1]]-bs_y)**2 + (z[tentative_CH[x1]]-bs_z)**2)**(1/2)
    radius.input['energy']=1.0
    radius.input['dist_to_base']=dist
    radius.compute()
    comp_rad.append(radius.output['comp_radius'])
ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=150)
for x1 in range(0,len(tentative_CH)):
    print('[ {0} {1} {2} {3} {4} ]'.format(tentative_CH[x1],x[tentative_CH[x1]], y[tentative_CH[x1]],z[tentative_CH[x1]],comp_rad[x1]))
