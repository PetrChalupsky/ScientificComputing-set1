import matplotlib.pyplot as plt
import numpy as np
string_1 = np.load('data/string_1.npy')
string_2 = np.load('data/string_2.npy')
string_3 = np.load('data/string_3.npy')

fig, axes = plt.subplots(1,3, sharey=True,figsize=(15,5),constrained_layout=True)

im0 = axes[0].imshow(string_1, origin='lower')
im1 = axes[1].imshow(string_2,origin='lower')
im2 = axes[2].imshow(string_3, origin='lower')
fig.colorbar(im0, ax=axes[:], fraction=0.016, pad=0.01)

axes[0].set_ylabel('Time', fontsize=14)
axes[1].set_xlabel('$x$-coordinate', fontsize=14)
axes[0].set_title('A') # Initial conditions a=5, piecewise (viz assignment instructions)
axes[1].set_title('B') # Initial conditions a=5
axes[2].set_title('C') # Initial conditions a=2

fig.savefig("results/vibrating_string", dpi=300, bbox_inches='tight')
