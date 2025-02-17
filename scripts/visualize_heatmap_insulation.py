"""Visualization of primitive insulation"""
import matplotlib.pyplot as plt
import numpy as np

grid_insulation = np.load("data/primitive_insulation_steady.npy")

plt.imshow(grid_insulation, origin='lower')
plt.colorbar()
plt.savefig("results/heatmap_primitive_insulation", dpi=300)