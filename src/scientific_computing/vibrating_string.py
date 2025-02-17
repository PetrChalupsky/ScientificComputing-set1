"""Solves the vibrating string for different initial conditions"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def solve_vibrating_string(dx, dt, L=1, t=1, c=1, a=5, piecew=False):
    """Solves the wave equation for a 1D string

    Args:
        dx (float): Step size in x dimension
        dt (float): Step size in time dimension
        L (float): Length of the string
        t (float): Simulation time
        c (float): Constant in the wave equation
        a (float): Parameter to scale the argument of an IC function
        piecew (boolean): If True, chooses piecewise initial condition instead
        of pure sin function
    Returns:
        u (2D array): The spatio-temporal solution of the 1D equation
    """
    r = (c * dt / dx) ** 2
    nx = int(L / dx + 1)  # number of columns
    nt = int(t / dt + 1)  # number of rows
    x = np.linspace(0, L, nx)
    u = np.zeros((nt, nx))

    # ICs
    if piecew == False:
        u[0, :] = np.sin(a * pi * x)
    else:
        for i, position in enumerate(x):
            if 1 / 5 < position < 2 / 5:
                u[0, i] = np.sin(a * pi * position)
            else:
                u[0, i] = 0

    if u[0, 0] > 0.0001 or u[0, -1] > 0.0001:
        print("Boundary conditions not fulfilled")

    u[1, 1:-1] = u[0, 1:-1] + 0.5 * r * (u[0, 2:] - 2 * u[0, 1:-1] + u[0, :-2])

    for n in range(1, nt - 1):
        u[n + 1, 1:-1] = (
            2 * u[n, 1:-1]
            - u[n - 1, 1:-1]
            + r * (u[n, 2:] - 2 * u[n, 1:-1] + u[n, :-2])
        )

    return u


def plot_vibrating_string(u, L, t):
    """Plots the solution of 1D wave equation for a string"""
    plt.imshow(u, extent=[0, L, t, 0])
    plt.xlabel("x")
    plt.ylabel("Time")
    plt.colorbar(label="Amplitude")

    plt.savefig("results/vibrating_string")


def animate_string(u, x):
    """Animates the solution of 1D wave equation for a string"""
    fig, ax = plt.subplots()
    (line,) = ax.plot([], [])
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(np.min(u), np.max(u))
    ax.set_xlabel("x")
    ax.set_ylabel("Time")

    def update(frame):
        line.set_data(x, u[frame, :])
        return [line]

    anim = animation.FuncAnimation(
        fig=fig, func=update, frames=u.shape[0], interval=30, blit=True
    )

    anim.save("results/animate_string.mp4")
    return anim
