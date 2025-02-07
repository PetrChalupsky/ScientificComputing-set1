"""
This code contains functions to calculate and visualize concentration diffusion
over a square grid, using the time dependent diffusion equation.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import erfc
from numba import njit

def initialize_grid(width):
    """
    Initialize grid given a width as parameter. It assumes a square grid.
    The upper row is equal to 1. The rest of the grid is equal to 0.
    """
    #Set empty grid
    c = np.zeros((width, width))

    #Set upper and lower boundary conditions
    c[width-1, :] = 1

    return c

#@njit
def update_grid(width, dt, grid, D):
    """
    Updates grid according to explicit scheme derived from the
    time dependent diffusion equation.
    """

    dx = 1/width

    factor = dt*D / dx**2

    # For each cell calculate new value with the explicit scheme.
    for i in range(1, width-1):
        for j in range(width):
            grid[i, j] = grid[i, j] + factor * (grid[(i+1) % (width), j] + 
                                                grid[(i-1) % (width), j] +
                                                grid[i, (j-1) % (width)] +
                                                grid[i, (j+1) % (width)] -
                                                4*grid[i,j])

    return grid


def time_dep_diff(width, D, dt, t):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """
    dx = 1/width

    # Check if the scheme is stable.
    if 4*dt*D / dx**2 > 1:
        raise ValueError("The scheme is not stable")

    # Number of timesteps
    steps = int(t/dt)

    # Initialize the grid
    grid = initialize_grid(width)

    # Update the grid for calculated amount of steps
    step = 0

    for step in range(steps):
        grid = update_grid(width, dt, grid, D)
        step = step+1
    
    return grid

def analytical_solution(D, t):
    """
    Calculates analytical solution of time dependent diffusion equation
    assuming y between 0 and 1.
    """

    y = np.linspace(0, 1, 50)
    solution = np.zeros_like(y)

    i_values = np.arange(0, 10000)
    sqrt_term = 2 * np.sqrt(D * t)

    for k in range(50):  
        solution[k] = np.sum(
            erfc((1 - y[k] + 2 * i_values) / sqrt_term) - 
            erfc((1 + y[k] + 2 * i_values) / sqrt_term)
        )
    return solution

def visualize_comparison(width, D, dt):
    """
    Returns figure for the comparison of the numerical and analytical
    solution of the time dependent diffusion equation for multiple values of time.
    """
    times = [0.001, 0.01, 0.1, 1]

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    i = 0

    fig = plt.figure(figsize=(8, 6))
    for time in times:
        grid = time_dep_diff(width, D, dt, time)
        concentration_y = np.sum(grid, axis=1) / width
        plt.plot(np.linspace(0, 1, width), concentration_y, label='t=' + str(time), color=colors[i])
        plt.plot(np.linspace(0, 1, 50), analytical_solution(1, time), linestyle='--', label='Analytical t=' + str(time), color=colors[i])
        i = i + 1
    
    plt.title('Comparison of Concentration with Analytical Solution', fontsize=14)
    plt.xlabel('$y$-coordinate', fontsize=14)
    plt.ylabel('Concentration', fontsize=14)
    plt.legend(fontsize=14)

    return fig

def heatmap_plot(width, D, dt):
    """
    Calculate the concentration on a square grid and generate 
    heatmaps for multiple times. 
    """

    times = [0, 0.001, 0.01, 0.1, 1]

    fig2, axes = plt.subplots(2, 3, figsize=(10, 6)) 
    cbar_ax = fig2.add_axes([0.92, 0.15, 0.02, 0.7])

    for i, time in enumerate(times):
        row, col = divmod(i, 3)  
        grid = time_dep_diff(width, D, dt, time)
        im = axes[row, col].imshow(grid, origin='lower', cmap='inferno', extent=[0,1,0,1])
        axes[row, col].set_title('t=' + str(time))
    
    axes[1,2].axis('off')

    fig2.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

    fig2.colorbar(im, cax=cbar_ax)
    fig2.suptitle("Heatmap of Concentration for multiple Time Values", fontsize=14)
    fig2.supxlabel("$x$-coordinate", fontsize=14)
    fig2.supylabel("$y$-coordinate", fontsize=14)
    return fig2

def animation(width, D, dt, total_time):
    """
    Make an animation of the heatmap of the time dependent diffusion equation
    over time until a steady state is reached. 
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Initial grid
    grid = time_dep_diff(width, D, dt, 0)
    im = ax.imshow(grid, origin='lower', cmap='inferno', extent=[0,1,0,1])

    ax.set_title("Heatmap of Diffusion over Time", fontsize=14)
    ax.set_xlabel("$x$-coordinate", fontsize=14)
    ax.set_ylabel("$y$-coordinate", fontsize=14)
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
D = 1
dt = 0.0001

fig1 = visualize_comparison(width, D, dt)
fig1.savefig("time_dep_diff_comparison_1.png", dpi=300)

fig2 = heatmap_plot(width, D, dt)
fig2.savefig("time_dep_diff_heatmaps.png", dpi=300)

#t = 1
#ani = animation(width, D, dt, t)
#ani.save("time_dep_diff_animation.gif", dpi=300)