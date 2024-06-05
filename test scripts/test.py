import sys
from diffeq import solve_diffeq_1cc
import numpy as np
import matplotlib.pyplot as plt
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
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=event1cc, rtol=1e-6, atol=1e-9)
    return sol

def event1cc(t, h, lambda1):
    return h[0] - lambda1(t)

def mainfunc(h0):
    lambda1 = lambda t: t * 0
    t = 10000000000
    sol = solve_diffeq_1cc(h0, t, lambda1)
    fht = sol.t[-1]
    return fht

#generating x=h0 y=fht
if __name__ == "__main__":
    print(cpu_count())
    print(sys.executable)
    print(sys.version)
    print(sys.version_info)

    harr = np.arange(-10, 10.1, 0.1)
    T_values = []

    pool = Pool()
    T_values = pool.map(mainfunc, harr)
    pool.close()
    pool.join()

    A_values = []
    for i in range(len(harr)):
        delta = T_values[i] - ((harr[i] ** 2)/4)
        A_values.append(delta)

    # plt.figure(figsize=(8, 6), dpi=200)
    # for h, T in zip(harr, T_values):
    #     if T == 10000000000:
    #         plt.plot(h, 0, 'o', color='red')
    #         print(f"{h} failed")
    #     else:
    #         plt.plot(h, T, 'o', color='blue')
    #         print(h)
    # plt.title("λ(t) = t")
    # plt.xlabel("h0")
    # plt.ylabel("fht")
    # plt.show()
    # # plt.savefig('1.png')
    # plt.close()
    #
    # # plt.figure(figsize=(8, 6), dpi=200)
    # # plt.scatter(harr, A_values, color='red')
    # # plt.title("error between numerical and analytical solutions")
    # # plt.xlabel("error")
    # # plt.ylabel("h0")
    # # plt.show()
    # # plt.savefig('2.png')
    # # plt.close()

    #OR

    fig, axs = plt.subplots(2, figsize=(8, 12), dpi=400)

    # Plotting the first subplot with harr and T_values
    axs[0].plot(harr, T_values, 'o', color='blue')
    axs[0].set_title("λ(t) = 0")
    axs[0].set_xlabel("h0")
    axs[0].set_ylabel("fht")

    # Plotting the second subplot with harr and A_values
    axs[1].scatter(harr, A_values, color='red')
    axs[1].set_title("error between numerical and analytical solution for each h0")
    axs[1].set_xlabel("harr")
    axs[1].set_ylabel("A_values")

    plt.tight_layout()
    plt.show()
    plt.close()