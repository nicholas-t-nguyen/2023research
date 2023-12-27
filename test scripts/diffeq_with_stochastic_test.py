from diffeq_with_stochastic import diffeq_random_walk, diffeq_brownian_motion
import numpy as np
from matplotlib import pyplot as plt


t = 100
steps = 1000
t_eval = np.linspace(0, t, steps + 1)

plt.figure(figsize=(8, 6))

sol = diffeq_random_walk(t, steps, 10)
plt.plot(sol.t, sol.y[0])

plt.xlabel('t')
plt.ylabel('Bt')

plt.show()