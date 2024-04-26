from diffeq import solve_diffeq_2cc
from firsthittingtime import fht2cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import multiprocessing
import inspect
import csv

t = 10
steps = 5000
dt = t / steps
t_eval = np.arange(0, t + dt, dt)
h0 = 1.5

plt.figure(figsize=(8, 6), dpi=400)

lambda1 = lambda t: 2 * np.sqrt(t) + 1
lambda2 = lambda t: -2 * np.sqrt(t) - 1

if __name__ == "__main__":
    sol = solve_diffeq_2cc(t, steps, h0, lambda1, lambda2)

    solinterp = interp1d(t_eval, sol.y[0])
    fhtv, fhtl = fht2cc(solinterp, lambda1, lambda2, t, dt)

    plt.plot(t_eval, [solinterp(t) for t in t_eval], color='black')
    plt.plot(t_eval, [lambda1(t) for t in t_eval], color='gold')
    plt.plot(t_eval, [lambda2(t) for t in t_eval], color='green')
    plt.scatter(fhtv, solinterp(fhtv), color='blue')
    # plt.xlim((fhtv-0.1, fhtv+0.1))
    # plt.ylim((solinterp(fhtv)-1, solinterp(fhtv)+1))
    print(fhtv)
    plt.show()
    plt.close()
