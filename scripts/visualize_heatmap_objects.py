import matplotlib.pyplot as plt
import numpy as np
grid_no_object = np.load("data/grid_no_object_steady.npy")
grid_object1 = np.load("data/grid_object1_steady.npy")
grid_object2 = np.load("data/grid_object2_steady.npy")


fig, axes = plt.subplots(1,3, sharey=True,figsize=(15,5),constrained_layout=True)

im0 = axes[0].imshow(grid_no_object, origin='lower')
im1 = axes[1].imshow(grid_object1,origin='lower')
im2 = axes[2].imshow(grid_object2, origin='lower')
fig.colorbar(im0, ax=axes[:], fraction=0.02, pad=0.01)

axes[0].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[1].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[2].xaxis.set_ticks(np.arange(0, 19, 2.5))
axes[0].set_ylabel('$y$-coordinate', fontsize=14)
axes[1].set_xlabel('$x$-coordinate', fontsize=14)
axes[0].set_title('No object')
axes[1].set_title('Rectangle')
axes[2].set_title('Multiple rectangles')

fig.savefig("results/heatmap_objects", dpi=300, bbox_inches='tight')


