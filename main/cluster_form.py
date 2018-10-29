from deploy import *
from fuzzy_radius import *


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Axis labels set
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(bs_x, bs_y, bs_z, c='r', marker='^', s=500)
ax.scatter(x,y,z,c='b')
ax.scatter(x_dup,y_dup,z_dup,c='r', marker='*', s=150)
fig.suptitle(' Fig 2. Initial Cluster Head Selection',fontsize=20,color='c')

simul_no = 10

cluster_count =dict.fromkeys(in_final_CH,1)
cluster = {}

for i in range(N):
    if is_CH[i] == False:
        sd = np.inf
        for j in range(len(in_final_CH)):
            ind= in_final_CH[j]
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
                    #print(e)
                    ener[i] = e
                    #print(ener[i])
            #print(ener[i])
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
                    #print(e)
                    ener[i] = e
            #print(ener[i])
#print(ener)
