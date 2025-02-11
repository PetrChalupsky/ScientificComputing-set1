"""
This code contains functions to compare iteration methods that compute 
diffusion over a square grid, using the Laplace equation.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from numba import njit

@njit
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

def jacobi_iteration(width, eps):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width-1):
            for j in range(width):
                new_grid[i, j] = 0.25 * (grid[(i+1) % (width), j] + 
                                         grid[(i-1) % (width), j] +
                                         grid[i, (j-1) % (width)] +
                                         grid[i, (j+1) % (width)])
        
        delta = np.max(np.abs(new_grid-grid))
        delta_list.append(delta)
        k = k + 1

    return new_grid, k, delta_list

def gauss_seidel(width, eps):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width-1):
            for j in range(width):
                new_grid[i, j] = 0.25 * (new_grid[(i+1) % (width), j] + 
                                         new_grid[(i-1) % (width), j] +
                                         new_grid[i, (j-1) % (width)] +
                                         new_grid[i, (j+1) % (width)])
        
        delta = np.max(np.abs(new_grid-grid))
        delta_list.append(delta)
        k = k + 1
    
    return new_grid, k, delta_list

@njit
def sor(width, eps, omega):
    """
    Given the input makes an initial grid and updates this
    for a given time. Returns final grid.
    """

    # Initialize the grid
    new_grid = initialize_grid(width)

    # Update grid while difference larger than epsilon
    delta = 100
    delta_list = []
    k = 0
    while delta >= eps:
        grid = new_grid.copy()
        for i in range(1, width-1):
            for j in range(width):
                new_grid[i, j] = 0.25 * omega * (new_grid[(i+1) % (width), j] + 
                                                 new_grid[(i-1) % (width), j] +
                                                 new_grid[i, (j-1) % (width)] +
                                                 new_grid[i, (j+1) % (width)]) + (1 - omega) * new_grid[i, j]
        
        delta = np.max(np.abs(new_grid-grid))
        delta_list.append(delta)
        k = k + 1
    
    return new_grid, k, delta_list

def analytical_solution(D, t):
    """
    Calculates analytical solution of time dependent diffusion equation
    assuming y between 0 and 1.
    """

    y = np.linspace(0, 1, 51)
    solution = np.zeros_like(y)

    for k in range(51):
        for i in range(5000):
            solution[k] += erfc((1-y[k]+(2*i))/(2*np.sqrt(D*t))) - erfc((1+y[k]+(2*i))/(2*np.sqrt(D*t)))

    return solution

def visualize_comparison(width, eps):
    """
    Returns figure for the comparison between the numerical and analytical
    solution of the Laplace equation using multiple iteration schemes.
    """

    fig = plt.figure(figsize=(8, 6))
    
    jacobi_grid = jacobi_iteration(width, eps)[0]
    jacobi_y = np.sum(jacobi_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), jacobi_y, label='Jacobi')

    gauss_seidel_grid = gauss_seidel(width, eps)[0]
    g_s_y = np.sum(gauss_seidel_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), g_s_y, label='Gauss-Seidel')

    sor_grid = sor(width, eps, 1.71)[0]
    sor_y = np.sum(sor_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.71$')

    sor_grid = sor(width, eps, 1.81)[0]
    sor_y = np.sum(sor_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.81$')

    sor_grid = sor(width, eps, 1.91)[0]
    sor_y = np.sum(sor_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.91$')
    
    plt.plot(np.linspace(0, 1, 51), analytical_solution(1, 1), linestyle='--', label='Analytical')
        
    
    plt.title('Comparison of Iteration Methods with Analytical Solution', fontsize=14)
    plt.xlabel('$y$-coordinate', fontsize=14)
    plt.ylabel('Concentration', fontsize=14)
    plt.legend(fontsize=14)

    return fig

def visualize_comparison_delta(width, eps):
    """
    Returns figure for the comparison between the numerical and analytical
    solution of the Laplace equation using multiple iteration schemes.
    """

    fig = plt.figure(figsize=(8, 6))
    
    k = jacobi_iteration(width, eps)[1]
    delta_list = jacobi_iteration(width, eps)[2]
    plt.plot(np.linspace(1, k, k), delta_list, label='Jacobi')

    k = gauss_seidel(width, eps)[1]
    delta_list = gauss_seidel(width, eps)[2]
    plt.plot(np.linspace(1, k, k), delta_list, label='Gauss-Seidel')

    k = sor(width, eps, 1.71)[1]
    delta_list = sor(width, eps, 1.71)[2]
    plt.plot(np.linspace(1, k, k), delta_list, label=r'SOR $\omega=1.71$')

    k = sor(width, eps, 1.81)[1]
    delta_list = sor(width, eps, 1.81)[2]
    plt.plot(np.linspace(1, k, k), delta_list, label=r'SOR $\omega=1.81$')

    k = sor(width, eps, 1.91)[1]
    delta_list = sor(width, eps, 1.91)[2]
    plt.plot(np.linspace(1, k, k), delta_list, label=r'SOR $\omega=1.91$')
            
    
    plt.title('Convergence Measure versus Number of Iterations', fontsize=14)
    plt.xlabel('$k$', fontsize=14)
    plt.ylabel(r'$\delta$', fontsize=14)
    plt.yscale('log')
    plt.legend(fontsize=14)

    return fig

def visualize_optimal_omega(width, eps):
    """
    Returns figure for the optimal value of omega versus the width of the grid.
    """

    def optimal_omega(width, eps):
        omega_list = np.arange(1.7, 1.999, 0.001)
        num_iterations = []

        for omega in omega_list:
            k = sor(width, eps, omega)[1]
            num_iterations.append(k)
        
        index = num_iterations.index(min(num_iterations))


        return omega_list[index]


    fig = plt.figure(figsize=(8, 6))
    
    list_N = [20, 30, 40, 50, 60, 70, 80]
    list_omega = []

    for N in list_N:
        omega = optimal_omega(N, eps)
        list_omega.append(omega)


    plt.plot(list_N, list_omega, 'o-')      
    
    plt.title('Optimal Omega versus Width of Grid', fontsize=14)
    plt.xlabel('$N$', fontsize=14)
    plt.ylabel(r'$\omega$', fontsize=14)

    return fig

# Figures 
width = 50
eps = 0.00001

fig1 = visualize_comparison(width, eps)
fig1.savefig("results/iteration_methods_comparison.png", dpi=300)

fig2 = visualize_comparison_delta(width, eps)
fig2.savefig("results/iteration_methods_delta_comparison.png", dpi=300)

fig3 = visualize_optimal_omega(width, eps)
fig3.savefig("results/sor_optimal_omega.png", dpi=300)
