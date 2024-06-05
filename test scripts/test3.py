import sys
from diffeq import solve_diffeq_1cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from multiprocessing import Pool, cpu_count
import inspect
import csv
import numpy as np
from scipy.integrate import solve_ivp
import imageio
import os


def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))


def solve_diffeq_1cc(h0, t, lambda1):
    event1cc.terminal = True
    event1cc.direction = 0
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=event1cc, rtol=1e-6, atol=1e-9)
    return sol


def event1cc(t, h, lambda1):
    return h[0] - lambda1(t)


def mainfunc(args):
    h0, c, n = args
    lambda1 = lambda t: n + t * c
    t = 10000000000
    sol = solve_diffeq_1cc(h0, t, lambda1)
    fht = sol.t[-1]
    return fht


# generating x=h0 y=fht
if __name__ == "__main__":
    print(cpu_count())
    harr = np.arange(-10, 10.1, 0.1)
    narr = np.arange(-10, 11, 1)
    carr = np.logspace(-6, 6, 130)
    filenames = []

    for c in carr:
        for i, n in enumerate(narr):
            T_values = []

            args = [(h, c, n) for h in harr]

            pool = Pool()
            T_values = pool.map(mainfunc, args)
            pool.close()
            pool.join()

            plt.figure(figsize=(8, 6), dpi=200)
            for h, T in zip(harr, T_values):
                if T == 10000000000:
                    plt.plot(h, 0, 'o', color='red')
                    print(f"{h} failed")
                else:
                    plt.plot(h, T, 'o', color='blue')
            plt.title(f"λ(t) = {n} + t * {c}")
            plt.xlabel("h0")
            plt.ylabel("fht")

            filename = f"plot_n{n}_c{i}.png"
            filenames.append(filename)
            plt.savefig(filename)
            plt.close()

    with imageio.get_writer('plots.gif', mode='I', duration=0.5) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)

    for filename in filenames:
        os.remove(filename)