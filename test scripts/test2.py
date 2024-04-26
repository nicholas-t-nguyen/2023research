from diffeq import solve_diffeq_1cc
from firsthittingtime import fht1cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import multiprocessing
import inspect
import csv


plt.figure(figsize=(8, 6), dpi=400)

lambda1 = lambda t: 2 * np.sqrt(t) + 1

if __name__ == "__main__":
    t = 0.08
    steps = 100
    dt = t / steps
    t_eval = np.arange(0, t + dt, dt)
    h0 = 2

    sol = solve_diffeq_1cc(t, steps, h0, lambda1)

    solinterp = interp1d(t_eval, sol.y[0])
    fhtv = fht1cc(solinterp, lambda1, t, dt)
    print(fhtv)

    plt.plot(t_eval, [solinterp(t) for t in t_eval], color='black')
    plt.plot(t_eval, [lambda1(t) for t in t_eval], color='gold')
    plt.scatter(fhtv, solinterp(fhtv), color='blue')
    plt.xlim((0,0.2))
    plt.ylim((lambda1(fhtv)-0.5,lambda1(fhtv)+0.5))
    print(sol.y)
    plt.show()
    plt.close()
