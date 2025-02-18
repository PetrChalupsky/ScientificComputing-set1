"""
Course: Scientific computing
Names: Lisa Pijpers, Petr Chalupský and Tika van Bennekum
Student IDs: 15746704, 15719227 and 13392425

File description:
    Computes optimal omega for grid with objects.
"""

import numpy as np
from scientific_computing.add_object_SOR import (
    calculate_optimal_omega,
    calculate_optimal_omega_objects,
)

# Define two different (sets of) objects
list_objects1 = np.array([[3, 8, 4, 10]], dtype=np.int64)
list_objects2 = np.array(
    [[7, 12, 15, 18], [14, 17, 2, 5], [4, 5, 4, 8]], dtype=np.int64
)

list_N = np.array([20, 30, 40, 50, 60, 70, 80], dtype=np.int64)

eps = 0.00001

list_omega_object1 = calculate_optimal_omega_objects(eps, list_objects1, list_N)
list_omega_object2 = calculate_optimal_omega_objects(eps, list_objects2, list_N)
list_omega = calculate_optimal_omega(eps, list_N)

np.save("data/list_omega.npy", list_omega)
np.save("data/list_omega_object1.npy", list_omega_object1)
np.save("data/list_omega_object2.npy", list_omega_object2)
