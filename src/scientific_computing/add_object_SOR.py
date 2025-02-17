"""Adds objects (sinks) to 2D diffusion grid"""

import numpy as np
from numba import njit
from scientific_computing.laplace import initialize_grid, sor


@njit
def create_objects(list_objects, width):
    objects_grid = initialize_grid(width)
    for objects in list_objects:
        row_start, row_end, column_start, column_end = objects
        objects_grid[row_start:row_end, column_start:column_end] = 1
    return objects_grid


@njit
def sor_with_objects(width, eps, omega, objects):
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
                if objects[i, j] == 1:
                    new_grid[i, j] = 0
                else:
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


@njit
def optimal_omega_objects(width, eps, objects):
    omega_list = np.arange(1.1, 1.99, 0.01)
    num_iterations = []

    for omega in omega_list:
        k = sor_with_objects(width, eps, omega, objects)[1]
        num_iterations.append(k)

    # Find index of minimal number of iterations
    index = num_iterations.index(min(num_iterations))

    return omega_list[index]


@njit
def calculate_optimal_omega_objects(eps, list_objects, list_N):
    """
    Returns figure for the optimal value of omega versus the width of the grid.
    """

    width = int(list_N[0])
    objects = create_objects(list_objects, width)

    list_omega = []

    for N in list_N:
        omega = optimal_omega_objects(N, eps, objects)
        list_omega.append(omega)

    return list_omega


@njit
def optimal_omega(width, eps):
    omega_list = np.arange(1.1, 1.99, 0.01)
    num_iterations = []

    for omega in omega_list:
        k = sor(width, eps, omega)[1]
        num_iterations.append(k)

    # Find index of minimal number of iterations
    index = num_iterations.index(min(num_iterations))

    return omega_list[index]


@njit
def calculate_optimal_omega(eps, list_N):
    """
    Returns figure for the optimal value of omega versus the width of the grid.
    """

    list_omega = []

    for N in list_N:
        omega = optimal_omega(N, eps)
        list_omega.append(omega)
    return list_omega
