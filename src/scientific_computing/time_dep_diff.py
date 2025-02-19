"""
Course: Scientific computing
Names: Lisa Pijpers, Petr Chalupský and Tika van Bennekum
Student IDs: 15746704, 15719227 and 13392425

File description:
    Solves the time dependent diffusion.
"""

import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.special import erfc


def initialize_grid(width):
    """
    Initialize grid given a width as parameter. It assumes a square grid.
    The upper row is equal to 1. The rest of the grid is equal to 0.
    """
    # Set empty grid
    c = np.zeros((width, width))

    # Set upper and lower boundary conditions
    c[width - 1, :] = 1

    return c


# @njit
def update_grid(width, dt, grid, D):
    """
    Updates grid according to explicit scheme derived from the
    time dependent diffusion equation.
    """

    dx = 1 / width

    factor = dt * D / dx**2

    # Make a copy of the grid so that it does not overwrite the old grid
    new_grid = grid.copy()

    # For each cell calculate new value with the explicit scheme.
    for i in range(1, width - 1):
        for j in range(width):
            new_grid[i, j] = grid[i, j] + factor * (
                grid[(i + 1) % (width), j]
                + grid[(i - 1) % (width), j]
                + grid[i, (j - 1) % (width)]
                + grid[i, (j + 1) % (width)]
                - 4 * grid[i, j]
            )

    return new_grid


def time_dep_diff(width, D, dt, t):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """
    dx = 1 / width

    # Check if the scheme is stable.
    if 4 * dt * D / dx**2 > 1:
        raise ValueError("The scheme is not stable")

    # Number of timesteps
    steps = int(t / dt)

    # Initialize the grid
    grid = initialize_grid(width)

    # Update the grid for calculated amount of steps
    step = 0

    for step in range(steps):
        grid = update_grid(width, dt, grid, D)
        step = step + 1

    return grid


def analytical_solution(D, t):
    """
    Calculates analytical solution of time dependent diffusion equation
    assuming y between 0 and 1.
    """

    y = np.linspace(0, 1, 50)
    solution = np.zeros_like(y)

    i_values = np.linspace(0, 10000, 10001)
    sqrt_term = 2 * np.sqrt(D * t)

    for k in range(50):
        solution[k] = np.sum(
            erfc((1 - y[k] + 2 * i_values) / sqrt_term)
            - erfc((1 + y[k] + 2 * i_values) / sqrt_term)
        )
    return solution
