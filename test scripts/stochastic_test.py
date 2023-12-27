import numpy as np
from stochastic import brownian_motion, random_walk
from matplotlib import pyplot as plt
from multiprocessing import Process

plt.figure(figsize=(8, 6))

t = 10
steps = 100
x = random_walk(t ,steps)
y = random_walk(t ,steps)

t = np.linspace(0, t, steps + 1)

plt.plot(t, y)
plt.xlim(0)
plt.xlabel('t')
plt.ylabel('Bt')

plt.show()

