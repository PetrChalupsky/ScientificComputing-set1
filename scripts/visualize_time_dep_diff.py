"""
This code contains functions to calculate and visualize concentration diffusion
over a square grid, using the time dependent diffusion equation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
from scientific_computing.time_dep_diff import time_dep_diff


def visualize_comparison(width):
    """
    Returns figure for the comparison of the numerical and analytical
    solution of the time dependent diffusion equation for multiple values of time.
    """

    # t=0 is not included since the analytical solution cannot be calculated for t=0
    times = [0.001, 0.01, 0.1, 1]
    grid = {}
    analy_sol = {}
    for i, time in enumerate(times):
        grid[i] = np.load(f"data/time_dep_diff_{time}.npy")
        analy_sol[i] = np.load(f"data/time_dep_diff_analy_{time}.npy")

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    i = 0

    fig = plt.figure(figsize=(8, 6))
    for i, time in enumerate(times):
        concentration_y = np.sum(grid[i], axis=1) / width
        plt.plot(
            np.linspace(0, 1, width),
            concentration_y,
            label="t=" + str(time),
            color=colors[i],
        )

        plt.plot(np.linspace(0, 1, width), analy_sol[i], linestyle="--")
        i = i + 1

    handles, labels = plt.gca().get_legend_handles_labels()
    custom_label = Line2D(
        [0], [0], linestyle="--", color="black", label="Analytical sol."
    )

    handles.append(custom_label)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$y$-coordinate", fontsize=18)
    plt.ylabel("Concentration", fontsize=18)
    plt.legend(handles=handles, fontsize=18)

    return fig


def heatmap_plot():
    """
    Calculate the concentration on a square grid and generate
    heatmaps for multiple times.
    """
    times = [0, 0.001, 0.01, 0.1, 1]
    grid = {}
    for i, time in enumerate(times):
        grid[i] = np.load(f"data/time_dep_diff_{time}.npy")

    fig2, axes = plt.subplots(2, 3, figsize=(10, 6), sharey=True)

    # Reduce spacing between subplots
    plt.subplots_adjust(wspace=-0.01, hspace=0.25)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    for i, time in enumerate(times):
        row, col = divmod(i, 3)
        im = axes[row, col].imshow(
            grid[i], origin="lower", cmap="inferno", extent=[0, 1, 0, 1]
        )
        axes[row, col].set_title("t=" + str(time))

    axes[1, 2].axis("off")

    fig2.colorbar(im, ax=axes[:, :], fraction=0.05, pad=0.025)
    fig2.supxlabel("$x$-coordinate", fontsize=18)
    fig2.supylabel("$y$-coordinate", fontsize=18, x=0.1)

    return fig2


def animation(width, D, dt, total_time):
    """
    Make an animation of the heatmap of the time dependent diffusion equation
    over time until a steady state is reached.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    # Initial grid
    grid = time_dep_diff(width, D, dt, 0)
    im = ax.imshow(grid, origin="lower", cmap="inferno", extent=[0, 1, 0, 1])

    ax.set_xlabel("$x$-coordinate", fontsize=18)
    ax.set_ylabel("$y$-coordinate", fontsize=18)
    ax.tick_params(axis="both", which="major", labelsize=14)  # Set tick label size
    fig.colorbar(im, ax=ax)

    def animate(i):
        t = (i / 50) * total_time
        grid = time_dep_diff(width, D, dt, t)
        im.set_array(grid)
        return im

    ani = FuncAnimation(fig, animate, frames=50, repeat=False, interval=50, blit=False)

    return ani


# Figures and animation
width = 50

fig1 = visualize_comparison(width)
fig1.savefig("results/time_dep_diff_comparison_1.png", dpi=300)

fig2 = heatmap_plot()
fig2.savefig("results/time_dep_diff_heatmaps.png", dpi=300, bbox_inches="tight")

D = 1
dt = 0.0001
total_time = 1
ani = animation(width, D, dt, total_time)
ani.save("results/time_dep_diff_animation.gif", dpi=300)
