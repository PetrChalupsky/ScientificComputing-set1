"""Visualize optimal omega for Laplace equation with objects"""

import numpy as np
import matplotlib.pyplot as plt

list_omega = np.load("data/list_omega.npy")
list_omega_object1 = np.load("data/list_omega_object1.npy")
list_omega_object2 = np.load("data/list_omega_object2.npy")

fig = plt.figure(figsize=(8, 6))
list_N = [20, 30, 40, 50, 60, 70, 80]

plt.plot(list_N, list_omega_object1, "o-", label="Rectangle")
plt.plot(list_N, list_omega_object2, "o-", label="Multiple rectangles")
plt.plot(list_N, list_omega, "o-", label="No object")

plt.xlabel("$N$", fontsize=18)
plt.ylabel(r"$\omega$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)


fig.savefig("results/sor_with_objects_optimal_omega.png", dpi=300)
