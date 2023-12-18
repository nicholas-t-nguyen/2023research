import numpy as np
from stochastic import brownian_motion, random_walk
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 6))

x = random_walk(10,10000)
y = random_walk(10,10000)

t = np.linspace(0, 10, 1001)

plt.plot(x, y)

plt.xlabel('t')
plt.ylabel('Bt')

plt.show()