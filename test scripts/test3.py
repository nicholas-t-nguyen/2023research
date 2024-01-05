import numpy as np
import os
import multiprocessing as mp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from one_curve_case import solve_diffeq_scaled
from stochastic import brownian_motion

def get_color(i, total):
    cmap = plt.get_cmap('hsv')
    return cmap(i / total)
def plot(plotnum):
    print(f'{plotnum} starting')
    np.random.seed()
    t = 1000
    steps = 10000
    h0 = 10
    kappa = 1
    alpha = 1
    t_eval = np.linspace(0, t, steps + 1)

    plt.figure(figsize=(10, 8))

    bmv = brownian_motion(t, steps)
    bm = interp1d(x=t_eval, y=bmv)
    plt.plot(t_eval, bmv, label="Brownian motion", color='brown')

    range_alpha = np.linspace(0, 1, 11)

    for i in range(len(range_alpha)):
        sol = solve_diffeq_scaled(t, steps, h0, kappa, bm, range_alpha[i])
        color = get_color(i, len(range_alpha))
        plt.plot(sol.t, sol.y[0], label=f'α={range_alpha[i]}', color=color)

    box = plt.gca().get_position()
    plt.gca().set_position([box.x0, box.y0, box.width * 0.8, box.height])

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.title(f"Single curve case plot of multiple alpha at h0 = {h0}")

    plt.savefig(f'1cc/alpha{plotnum}.png')

    print(f'{plotnum} done')

if __name__ == "__main__":
    pool = mp.Pool(processes=2)
    pool.map(plot, range(1,6))
    pool.close()
    pool.join()