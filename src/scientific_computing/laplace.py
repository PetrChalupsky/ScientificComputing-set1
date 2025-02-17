"""
This code contains functions to compare iteration methods that compute 
diffusion over a square grid, using the Laplace equation.
"""

import numpy as np
from scipy.special import erfc
from numba import njit


@njit
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


def jacobi_iteration(width, eps):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width - 1):
            for j in range(width):
                new_grid[i, j] = 0.25 * (
                    grid[(i + 1) % (width), j]
                    + grid[(i - 1) % (width), j]
                    + grid[i, (j - 1) % (width)]
                    + grid[i, (j + 1) % (width)]
                )

        delta = np.max(np.abs(new_grid - grid))
        delta_list.append(delta)
        k = k + 1

    return new_grid, k, delta_list


def gauss_seidel(width, eps):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width - 1):
            for j in range(width):
                new_grid[i, j] = 0.25 * (
                    new_grid[(i + 1) % (width), j]
                    + new_grid[(i - 1) % (width), j]
                    + new_grid[i, (j - 1) % (width)]
                    + new_grid[i, (j + 1) % (width)]
                )

        delta = np.max(np.abs(new_grid - grid))
        delta_list.append(delta)
        k = k + 1

    return new_grid, k, delta_list


@njit
def sor(width, eps, omega):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width - 1):
            for j in range(width):
                new_grid[i, j] = (
                    0.25
                    * omega
                    * (
                        new_grid[(i + 1) % (width), j]
                        + new_grid[(i - 1) % (width), j]
                        + new_grid[i, (j - 1) % (width)]
                        + new_grid[i, (j + 1) % (width)]
                    )
                    + (1 - omega) * new_grid[i, j]
                )

        delta = np.max(np.abs(new_grid - grid))
        delta_list.append(delta)
        k = k + 1

    return new_grid, k, delta_list


def analytical_solution(D, t):
    """
    Calculates analytical solution of time dependent diffusion equation
    assuming y between 0 and 1.
    """

    y = np.linspace(0, 1, 51)
    solution = np.zeros_like(y)

    for k in range(51):
        for i in range(5000):
            solution[k] += erfc((1 - y[k] + (2 * i)) / (2 * np.sqrt(D * t))) - erfc(
                (1 + y[k] + (2 * i)) / (2 * np.sqrt(D * t))
            )

    return solution


def optimal_omega(width, eps):
    omega_list = np.arange(1.7, 1.999, 0.001)
    num_iterations = []

    for omega in omega_list:
        k = sor(width, eps, omega)[1]
        num_iterations.append(k)

    # Find index of minimal number of iterations
    index = num_iterations.index(min(num_iterations))

    return omega_list[index]
