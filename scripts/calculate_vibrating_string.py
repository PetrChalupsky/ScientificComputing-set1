"""Solves the vibrating string and stores the data"""

from scientific_computing.vibrating_string import (
    solve_vibrating_string,
    animate_string,
)
import numpy as np

h = 0.01
dt = h
dx = h
c = 1
L = 1
t = 1
nx = int(L / dx + 1)
x = np.linspace(0, L, nx)

u1 = solve_vibrating_string(dx, dt, L, t, c, a=5, piecew=True)
u2 = solve_vibrating_string(dx, dt, L, t, c)
u3 = solve_vibrating_string(dx, dt, L, t, c, a=2)

np.save("data/string_1.npy", u1)
np.save("data/string_2.npy", u2)
np.save("data/string_3.npy", u3)

animate_string(u3, x)