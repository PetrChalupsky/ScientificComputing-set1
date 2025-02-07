from scientific_computing.vibrating_string import solve_vibrating_string, plot_vibrating_string, animate_string
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

h = 0.01
dt = h
dx = h
c = 1
L = 1
t = 1
nx = int(L/dx +1)
x = np.linspace(0,L,nx)

u = solve_vibrating_string(dx,dt,L,t,c,a=5,piecew=True)
u = plot_vibrating_string(u,L,t)
u = solve_vibrating_string(dx, dt, L, t, c)
plot_vibrating_string(u,L,t)
u = solve_vibrating_string(dx,dt,L,t,c, a=2)
plot_vibrating_string(u,L,t)
animate_string(u,x)
