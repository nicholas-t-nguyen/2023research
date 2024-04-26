from diffeq import solve_diffeq_zerodriver
from firsthittingtime import fht1cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import multiprocessing
import inspect
import csv

t = 6
steps = 100
dt = t / steps
t_eval = np.arange(0, t + dt, dt)
h0 = 2

plt.figure(figsize=(8, 6), dpi=400)

zerodriver = lambda t: 0 * t

if __name__ == "__main__":
    sol = solve_diffeq_zerodriver(t, steps, h0)

    solinterp = interp1d(t_eval, sol.y[0])
    fhtv, fhtl = fht1cc(solinterp, zerodriver, t, dt)

    plt.plot(t_eval, [solinterp(t) for t in t_eval], color='black')
    plt.plot(t_eval, [zerodriver(t) for t in t_eval], color='gold')
    plt.scatter(fhtv, solinterp(fhtv), color='blue')
    # plt.xlim((fhtv-0.1, fhtv+0.1))
    # plt.ylim((solinterp(fhtv)-1, solinterp(fhtv)+1))
    print(fhtv)
    plt.show()
    plt.close()
