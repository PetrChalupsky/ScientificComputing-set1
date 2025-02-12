"""Visualization of primitive insulation"""
import matplotlib.pyplot as plt
import numpy as np

grid_insulation = np.load("data/primitive_insulation_steady.npy")



plt.imshow(grid_insulation, origin='lower')
plt.colorbar()
plt.savefig("results/heatmap_primitive_insulation", dpi=300)
#axes[0].xaxis.set_ticks(np.arange(0, 19, 2.5))
#axes[1].xaxis.set_ticks(np.arange(0, 19, 2.5))
#axes[2].xaxis.set_ticks(np.arange(0, 19, 2.5))
#axes[0].set_ylabel('$y$-coordinate', fontsize=14)
#axes[1].set_xlabel('$x$-coordinate', fontsize=14)
#axes[0].set_title('No object')
#axes[1].set_title('Rectangle')
#axes[2].set_title('Multiple rectangles')
#
#fig.savefig("heatmap_objects", dpi=300, bbox_inches='tight')
