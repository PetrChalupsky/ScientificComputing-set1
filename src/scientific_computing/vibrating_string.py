# 1.1 Vibrating string
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# write down discrete PDEs
# 

# ICs, BCs, step size and parameters
h = 0.01
dt = h
dx = h
c = 1
L = 1
t = 1


def solve_vibrating_string(dx, dt, L=1, t=1, c=1,a=5,piecew=False):
    r = (c*dt/dx)**2
    nx = int(L/dx + 1) # number of columns
    nt = int(t/dt + 1)# number of rows
    x = np.linspace(0,L,nx)
    u = np.zeros((nt, nx))
    
    
    # ICs
    if piecew == False:
        u[0,:] = np.sin(a*pi*x)
    else:
        for i, position in enumerate(x):
            if 1/5 < position < 2/5:
                print(position)
                u[0,i] = np.sin(a*pi*position)
            else:
                u[0,i] = 0 
            
    
    if u[0,0] !=0 or u[0,-1] !=0:
        print('Boundary conditions not fulfilled')
    
    
    u[1,1:-1] = u[0,1:-1] + 0.5*(r**2)* (u[0,2:] - 2*u[0,1:-1] + u[0,:-2])
    
    
    for n in range(1, nt-1):
        u[n+1, 1:-1] = 2*u[n, 1:-1] - u[n-1,1:-1] + r**2 * (u[n, 2:] - 2*u[n,1:-1] + u[n,:-2])

    return u

def plot_vibrating_string(u,L,t):
    plt.imshow(u,extent=[0,L,t,0])
    plt.colorbar()
    plt.show()

    #def animate_string(u,x):
    #    fig = plt.figure()
    #    def update(frame):
    #        print(u)
    #    
    #        plot = plt.plot(x,u[frame,:],color='blue')
    #        return plot
    #    
    #    
    #    animation.FuncAnimation(fig=fig,func=update, frames=40, interval=30,blit=True)
    #    plt.show()

def animate_string(u, x):
    fig, ax = plt.subplots()
    line, = ax.plot([], []) 
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(np.min(u), np.max(u))
    
    def update(frame):
        line.set_data(x, u[frame,:])
        return [line]
    
    
    anim = animation.FuncAnimation(
        fig=fig,
        func=update,
        frames=u.shape[0],  
        interval=30,
        blit=True
    )
    
    plt.show()
    return anim  

