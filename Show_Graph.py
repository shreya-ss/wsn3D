import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fuzzy_radius import *
from random import *


def show(ax,x_dup,y_dup,z_dup,final_comp_r):
    for i in range(0,len(x_dup)):
        r = final_comp_r[i]
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x11 =  r*np.outer(np.cos(u), np.sin(v))+x_dup[i]
        y11 =  r*np.outer(np.sin(u), np.sin(v))+y_dup[i]
        z11 =  r*np.outer(np.ones(np.size(u)), np.cos(v))+z_dup[i]
        sphere = ax.plot_surface(x11, y11, z11, color='g', edgecolor='none',alpha='0.10')