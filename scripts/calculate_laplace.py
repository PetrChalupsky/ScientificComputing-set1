"""Calculates steady state of Laplace equation and stores the results"""

import numpy as np
from scientific_computing.laplace import (
    sor,
    jacobi_iteration,
    gauss_seidel,
    optimal_omega,
)


eps = 0.00001
width = 50
jacobi_solution = jacobi_iteration(width, eps)
gauss_seidel_solution = gauss_seidel(width, eps)
sor_solution_171 = sor(width, eps, 1.71)
sor_solution_181 = sor(width, eps, 1.81)
sor_solution_191 = sor(width, eps, 1.91)

# Store grid for each iteration method
np.save("data/jacobi_grid.npy", jacobi_solution[0])
np.save("data/gauss_seidel_grid.npy", gauss_seidel_solution[0])
np.save("data/sor_grid_171.npy", sor_solution_171[0])
np.save("data/sor_grid_181.npy", sor_solution_181[0])
np.save("data/sor_grid_191.npy", sor_solution_191[0])

# Store number of iterations needed for each iteration method
np.save("data/jacobi_k.npy", jacobi_solution[1])
np.save("data/gauss_seidel_k.npy", gauss_seidel_solution[1])
np.save("data/sor_k_171.npy", sor_solution_171[1])
np.save("data/sor_k_181.npy", sor_solution_181[1])
np.save("data/sor_k_191.npy", sor_solution_191[1])

# Store list of delta values for each iteration method
np.save("data/jacobi_delta.npy", jacobi_solution[2])
np.save("data/gauss_seidel_delta.npy", gauss_seidel_solution[2])
np.save("data/sor_delta_171.npy", sor_solution_171[2])
np.save("data/sor_delta_181.npy", sor_solution_181[2])
np.save("data/sor_delta_191.npy", sor_solution_191[2])

# Calculate optimal omega for multiple grid sizes
list_N = [20, 30, 40, 50, 60, 70, 80]
list_omega = []

for N in list_N:
    omega = optimal_omega(N, eps)
    list_omega.append(omega)

np.save("data/list_omega_laplace.npy", list_omega)
np.save("data/list_N.npy", list_N)
