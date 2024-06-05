import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from multiprocessing import Pool, cpu_count
import inspect
import csv
import numpy as np
from scipy.integrate import solve_ivp

def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))

def solve_diffeq_1cc(h0, t, lambda1):
    event1cc.terminal = True
    event1cc.direction = 0
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=event1cc, rtol=1e-6, atol=1e-9, dense_output=True)
    return sol

def event1cc(t, h, lambda1):
    return h[0] - lambda1(t)

def mainfunc(h0):
    lambda1 = lambda t: t * 0
    t = 10000000000
    sol = solve_diffeq_1cc(h0, t, lambda1)
    fht = sol.t[-1]
    return fht, sol

#generating solution and driver plot
if __name__ == "__main__":
    fht, sol = mainfunc(-5)
    t = np.arange(0, fht+5, 0.0001)
    print(fht)
    plt.figure(figsize=(8, 6), dpi=200)
    plt.plot(t, [sol.sol(t) for t in t])
    # plt.plot(t, 0,color='gold')
    plt.ylim((-2, 5))
    plt.title("λ(t) = cos(t)")
    plt.show()
