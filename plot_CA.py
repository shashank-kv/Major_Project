import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as anim

rec=np.load('../../data/i0-0.5.npy')
ic=1
N = 100
trans=15;obs=15;T=trans+obs

tau_i = 4 
tau_r = 9
tau_0 = tau_i+tau_r

##Define discreet colormap
cmap = colors.ListedColormap(['xkcd:pale grey','xkcd:darkish red','xkcd:almost black'])
bounds = [0,0.99,tau_i+0.99,tau_0+0.99]
norm = colors.BoundaryNorm(bounds,cmap.N)

def animate(i):
    grid.set_data(rec[ic,i]) 
    ax.set_title("$t={}$".format(i+1))
    return grid,

if __name__=='__main__':
    fig,ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    grid=ax.imshow(rec[ic,0],origin='lower',cmap=cmap,norm=norm,interpolation='none')
    ani = anim.FuncAnimation(fig, animate, T, interval=100,repeat=False)
    plt.show()

