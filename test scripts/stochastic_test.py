import numpy as np
from stochastic import brownian_motion, random_walk
from matplotlib import pyplot as plt
from multiprocessing import Process

plt.figure(figsize=(8, 6))

def func():
    x = random_walk(100000000,100000000)
    y = random_walk(100000000,100000000)

    t = np.linspace(0, 100000000, 100000001)

    plt.plot(t, y)
    plt.xlim(0)
    plt.xlabel('t')
    plt.ylabel('Bt')

    plt.show()

if __name__ == '__main__':
    times = 10
    processes = []
    for _ in range(times):
        p = Process(target=func)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()