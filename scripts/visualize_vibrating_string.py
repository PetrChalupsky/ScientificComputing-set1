"""
Course: Scientific computing
Names: Lisa Pijpers, Petr Chalupský and Tika van Bennekum
Student IDs: 15746704, 15719227 and 13392425

File description:
    Visualizes the vibrating string heatmap solution.
"""

import matplotlib.pyplot as plt
import numpy as np

string_1 = np.load("data/string_1.npy")
string_2 = np.load("data/string_2.npy")
string_3 = np.load("data/string_3.npy")

fig, axes = plt.subplots(1, 3, sharey=True, figsize=(15, 5), constrained_layout=True)

# swapped string_1 with string_3 to do comment overleaf
im0 = axes[0].imshow(string_3, origin="lower", cmap="inferno")
im1 = axes[1].imshow(string_2, origin="lower", cmap="inferno")
im2 = axes[2].imshow(string_1, origin="lower", cmap="inferno")
cbar = fig.colorbar(im0, ax=axes[:], fraction=0.02, pad=0.01)
cbar.ax.tick_params(labelsize=14)  # Set colorbar tick label size


axes[0].set_ylabel("Time", fontsize=18)
axes[1].set_xlabel("$x$-coordinate", fontsize=18)
axes[0].set_title("A", fontsize=18)  # Initial conditions a=5, piecewise (viz assignment instructions)
axes[1].set_title("B", fontsize=18)  # Initial conditions a=5
axes[2].set_title("C", fontsize=18)  # Initial conditions a=2

for ax in axes:
    ax.tick_params(axis='both', which='major', labelsize=16)

fig.savefig("results/vibrating_string", dpi=300, bbox_inches="tight")
