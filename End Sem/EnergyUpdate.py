# -*- coding: utf-8 -*-
import numpy as np
from EnergyAwareClustering import Energy_Aware_Clustering
def energy_update(x,y,z,ener,N):
    
    bs_x = 100
    bs_y = 100
    bs_z = 5
    
    #total dead nodes yet
    d_count=0
    #round of transmissions for each node before dying
    round_of_transmission=[]
    for i in range(0,N):
        round_of_transmission.append(0);
   # print(round_of_transmission)
    
    while((d_count)<N):
        #Selection of Energy aware clustering and clusters
        Cluster_Head=Energy_Aware_Clustering(x,y,z,N,ener)
        
        #to check whether a node is Ch
        is_CH=[]
        
        for i in range(0,N):
            flag=0
            for j in range(0,len(Cluster_Head)):
                if(i==(Cluster_Head[j])):
                    flag=1;
                    break;
            if(flag==1):
                is_CH.append(1)
            else:
                is_CH.append(0)
        #print(is_CH)
        
        #cluster_count represents total nodes in a cluster for that CH
        cluster_count =dict.fromkeys(Cluster_Head,1)
        
        #cluster represents CH and their related nodes
        cluster = {}
    
        for i in range(N):
            if is_CH[i] == 0:
                sd = np.inf
                for j in range(len(Cluster_Head)):
                    ind= Cluster_Head[j]
                    d = ((x[i]-x[ind])**2 +(y[i]-y[ind])**2 + (z[i]-z[ind])**2)**(1/2)
                    if d < sd:
                        sd = d
                        sind = ind
                try:
                    cluster_count[sind] = cluster_count[sind]+1
                    cluster.setdefault(sind,[]).append(i)
                except KeyError:
                    pass 
    
        #Calculation of no of round
        
        no_of_round=20;
        
        
        
        #Update energy for next no_of_round
        for r in range(0,no_of_round):
            for i in range(N):
                if is_CH[i] == 1:
                    e = ener[i]
                    if e > 0:
                        dis = ((x[i]-bs_x)**2 + (y[i]-bs_y)**2 + (z[i]-bs_z)**2)**(1/2)
                        e = e - (( 51200 * (10 ** (-9))* (cluster_count[i]) ) + ( 102400 * (10 ** (-12)) * (dis ** 2)))
                        if e <= 0:
                            print('Node No: {0} , rounds: {1}'.format(i,round_of_transmission[i]))
                            
                            d_count = d_count + 1
                            ener[i]=-1
                        else:
                            ener[i] = e
                            
                            round_of_transmission[i]=round_of_transmission[i]+1
                    
                            
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
                            print('Node No: {0} , rounds: {1}'.format(i,round_of_transmission[i]))
                            d_count = d_count + 1
                            ener[i]=-1
                        else:
                            ener[i] = e
                            round_of_transmission[i]=round_of_transmission[i]+1
    