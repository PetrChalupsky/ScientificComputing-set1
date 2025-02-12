"""
This code contains functions to compare iteration methods that compute 
diffusion over a square grid, using the Laplace equation.
"""
import numpy as np
import matplotlib.pyplot as plt
from scientific_computing.laplace import analytical_solution
def visualize_comparison(width):
    """
    Returns figure for the comparison between the numerical and analytical
    solution of the Laplace equation using multiple iteration schemes.
    """

    jacobi_grid = np.load('data/jacobi_grid.npy')
    gauss_seidel_grid = np.load('data/gauss_seidel_grid.npy')
    sor_grid_171 = np.load('data/sor_grid_171.npy')
    sor_grid_181 = np.load('data/sor_grid_181.npy')
    sor_grid_191 = np.load('data/sor_grid_191.npy')

    fig = plt.figure(figsize=(8, 6))
    
    jacobi_y = np.sum(jacobi_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), jacobi_y, label='Jacobi')

    g_s_y = np.sum(gauss_seidel_grid, axis=1) / width
    plt.plot(np.linspace(0, 1, width), g_s_y, label='Gauss-Seidel')

    sor_y = np.sum(sor_grid_171, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.71$')

    sor_y = np.sum(sor_grid_181, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.81$')

    sor_y = np.sum(sor_grid_191, axis=1) / width
    plt.plot(np.linspace(0, 1, width), sor_y, label=r'SOR $\omega=1.91$')
    
    plt.plot(np.linspace(0, 1, 51), analytical_solution(1, 1), linestyle='--', label='Analytical')
        
    
    plt.xlabel('$y$-coordinate', fontsize=14)
    plt.ylabel('Concentration', fontsize=14)
    plt.legend(fontsize=14)

    return fig

def visualize_comparison_delta():
    """
    Returns figure for the comparison between the numerical and analytical
    solution of the Laplace equation using multiple iteration schemes.
    """

    jacobi_k = np.load('data/jacobi_k.npy')
    gauss_seidel_k = np.load('data/gauss_seidel_k.npy')
    sor_k_171 = np.load('data/sor_k_171.npy')
    sor_k_181 = np.load('data/sor_k_181.npy')
    sor_k_191 = np.load('data/sor_k_191.npy')
                                                                
    jacobi_delta = np.load('data/jacobi_delta.npy')
    gauss_seidel_delta = np.load('data/gauss_seidel_delta.npy')
    sor_delta_171 = np.load('data/sor_delta_171.npy')
    sor_delta_181 = np.load('data/sor_delta_181.npy')
    sor_delta_191 = np.load('data/sor_delta_191.npy')






    fig = plt.figure(figsize=(8, 6))
    
    plt.plot(np.linspace(1, jacobi_k, jacobi_k), jacobi_delta, label='Jacobi')
    plt.plot(np.linspace(1, gauss_seidel_k, gauss_seidel_k), gauss_seidel_delta, label='Gauss-Seidel')
    plt.plot(np.linspace(1, sor_k_171, sor_k_171), sor_delta_171, label=r'SOR $\omega=1.71$')
    plt.plot(np.linspace(1, sor_k_181, sor_k_181 ), sor_delta_181, label=r'SOR $\omega=1.81$')
    plt.plot(np.linspace(1, sor_k_191, sor_k_191), sor_delta_191, label=r'SOR $\omega=1.91$')
            
    
    plt.xlabel('$k$', fontsize=14)
    plt.ylabel(r'$\delta$', fontsize=14)
    plt.yscale('log')
    plt.legend(fontsize=14)

    return fig


def visualize_optimal_omega():
    """
    Returns figure for the optimal value of omega versus the width of the grid.
    """

    list_omega = np.load('data/list_omega_laplace.npy')
    list_N = np.load('data/list_N.npy') 
    
    fig = plt.figure(figsize=(8, 6))

    plt.plot(list_N, list_omega, 'o-')      
    
    plt.xlabel('$N$', fontsize=14)
    plt.ylabel(r'$\omega$', fontsize=14)

    return fig

# Figures 
width = 50
eps = 0.00001

fig1 = visualize_comparison(width)
fig1.savefig("results/iteration_methods_comparison.png", dpi=300)

fig2 = visualize_comparison_delta()
fig2.savefig("results/iteration_methods_delta_comparison.png", dpi=300)

fig3 = visualize_optimal_omega()
fig3.savefig("results/sor_optimal_omega.png", dpi=300)
