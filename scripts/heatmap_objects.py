"""Calculates steady state of Laplace equation with objects and stores the results"""

from scientific_computing.add_object_SOR import create_objects, sor_with_objects
import numpy as np
from scientific_computing.laplace import sor

# Define three different (sets of) objects
list_objects1 = np.array([[3, 8, 4, 10]], dtype=np.int64)
list_objects2 = np.array(
    [[7, 12, 15, 18], [14, 17, 2, 5], [4, 5, 4, 8]], dtype=np.int64
)
list_objects3 = np.array([[5, 6, 1, 19]], dtype=np.int64)

width = 20
eps = 0.00001
omega_no_object = 1.92
omega_object1 = 1.87
omega_object2 = 1.87

# Initialize the grids
objects1 = create_objects(list_objects1, width)
objects2 = create_objects(list_objects2, width)
primitive_insulation = create_objects(list_objects3, width)

# Calculate the steady state using SOR with and without objects
grid_no_object, _, _ = sor(width, eps, omega_no_object)
grid_object1, _, _ = sor_with_objects(width, eps, omega_object1, objects1)
grid_object2, _, _ = sor_with_objects(width, eps, omega_object2, objects2)
grid_primitive_insulation, _, _ = sor_with_objects(
    width, eps, omega_object2, primitive_insulation
)

np.save("data/grid_no_object_steady.npy", grid_no_object)
np.save("data/grid_object1_steady.npy", grid_object1)
np.save("data/grid_object2_steady.npy", grid_object2)
np.save("data/primitive_insulation_steady.npy", grid_primitive_insulation)