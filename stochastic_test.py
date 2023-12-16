import numpy as np

from stochastic import random_walk
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 6))

sol = random_walk(10,100)
t = np.arange(0, 10.1, .1)
print(t)
plt.plot(t, sol)
plt.xlim(0,10)


plt.xlabel('t')
plt.ylabel('Bt')

plt.show()