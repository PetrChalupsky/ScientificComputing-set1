"""
Course: Scientific computing
Names: Lisa Pijpers, Petr Chalupský and Tika van Bennekum
Student IDs: 15746704, 15719227 and 13392425

File description:
    Visualization of primitive insulation.
"""
import matplotlib.pyplot as plt
import numpy as np

grid_insulation = np.load("data/primitive_insulation_steady.npy")

plt.imshow(grid_insulation, origin='lower')
plt.colorbar()
plt.savefig("results/heatmap_primitive_insulation", dpi=300)