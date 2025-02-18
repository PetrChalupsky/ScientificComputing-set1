"""Visualization of steady state of Laplace equation with objects"""

import matplotlib.pyplot as plt
import numpy as np

grid_no_object = np.load("data/grid_no_object_steady.npy")
grid_object1 = np.load("data/grid_object1_steady.npy")
grid_object2 = np.load("data/grid_object2_steady.npy")


fig, axes = plt.subplots(1, 3, sharey=True, figsize=(15, 5), constrained_layout=True)

im0 = axes[0].imshow(grid_no_object, origin="lower", cmap="inferno")
im1 = axes[1].imshow(grid_object1, origin="lower", cmap="inferno")
im2 = axes[2].imshow(grid_object2, origin="lower", cmap="inferno")
cbar = fig.colorbar(im0, ax=axes[:], fraction=0.02, pad=0.01)
cbar.ax.tick_params(labelsize=14)  # Set colorbar tick label size

axes[0].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[1].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[2].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[0].set_ylabel("$y$-coordinate", fontsize=18)
axes[1].set_xlabel("$x$-coordinate", fontsize=18)
axes[0].set_title("No object", fontsize=16)
axes[1].set_title("Rectangle", fontsize=16)
axes[2].set_title("Multiple rectangles", fontsize=16)
for ax in axes:
    ax.tick_params(axis="both", which="major", labelsize=14)

fig.savefig("results/heatmap_objects", dpi=300, bbox_inches="tight")
