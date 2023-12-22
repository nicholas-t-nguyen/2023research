from diffeq_with_stochastic import diffeq_random_walk, diffeq_brownian_motion
import numpy as np
from matplotlib import pyplot as plt
import multiprocessing as mp

t = 100
steps = 1000
t_eval = np.linspace(0, t, steps + 1)

def func():
    plt.figure(figsize=(8, 6))

    sol = diffeq_random_walk(t, steps, 10)
    plt.plot(sol.t, sol.y[0])

    plt.xlabel('t')
    plt.ylabel('Bt')

    plt.show()
if __name__ == '__main__':
    mp.Process(target=func).start()
    mp.Process(target=func).start()
    mp.Process(target=func).start()
    mp.Process(target=func).start()
    mp.Process(target=func).start()