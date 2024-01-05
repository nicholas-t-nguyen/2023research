from diffeq_with_stochastic import solve_diffeq_random_walk, solve_diffeq_brownian_motion
import numpy as np
from matplotlib import pyplot as plt

t = 50
steps = 500
t_eval = np.linspace(0, t, steps + 1)

plt.figure(figsize=(8, 6))

sol = solve_diffeq_brownian_motion(t, steps, 10)
plt.plot(sol.t, sol.y[0])

plt.xlabel('t')
plt.ylabel('Bt')

plt.show()