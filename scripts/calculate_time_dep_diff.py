"""
Course: Scientific computing
Names: Lisa Pijpers, Petr Chalupský and Tika van Bennekum
Student IDs: 15746704, 15719227 and 13392425

File description:
    Runs time dependendent diffusion for couple selected time intervals.
"""

import numpy as np
from scientific_computing.time_dep_diff import time_dep_diff, analytical_solution

width = 50
D = 1
dt = 0.0001

times = [0, 0.001, 0.01, 0.1, 1]
for time in times:
    grid = time_dep_diff(width, D, dt, time)
    np.save(f"data/time_dep_diff_{time}", grid)

    # At t=0 it is not possible to calculate analytical solution
    if time == 0:
        continue

    analy_sol = analytical_solution(D, time)
    np.save(f"data/time_dep_diff_analy_{time}", analy_sol)

