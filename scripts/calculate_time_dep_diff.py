import numpy as np
import matplotlib.pyplot as plt
from scientific_computing.time_dep_diff import time_dep_diff, analytical_solution

width = 50
D = 1
dt = 0.0001

times = [0, 0.001, 0.01, 0.1, 1]
for time in times:
    grid = time_dep_diff(width, D, dt, time)
    analy_sol = analytical_solution(1,time)
    np.save(f'data/time_dep_diff_{time}',grid)
    np.save(f'data/time_dep_diff_analy_{time}',analy_sol )



