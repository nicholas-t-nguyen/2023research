from diffeq_with_stochastic import diffeq_brownian_motion
import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Pool


t = 100
steps = 1000
t_eval = np.linspace(0, t, steps + 1)

plt.figure(figsize=(8, 6))

iterable_values = [20, 10]
num_processes = 2

iterables = [[t, steps, i] for i in iterable_values]

if __name__ == '__main__':
    with Pool() as pool:
        solutions = pool.starmap(diffeq_brownian_motion, iterables)
    print(solutions)

    plt.figure(figsize=(8, 6))
    for sol in solutions:
        plt.plot(sol.t, sol.y[0])
        print(sol)

    plt.xlabel('t')
    plt.ylabel('Bt')
    plt.show()
