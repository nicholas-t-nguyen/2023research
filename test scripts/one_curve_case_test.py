from one_curve_case import solve_diffeq_scaled
import numpy as np
from matplotlib import pyplot as plt

t = 10
steps = 100
t_eval = np.linspace(0, t, steps + 1)
kappa = 1
alpha = 1

plt.figure(figsize=(8, 6))

sol = solve_diffeq_scaled(t, steps, 1 , kappa, alpha)
plt.plot(sol.t, sol.y[0])

plt.xlabel('t')
plt.ylabel('Bt')

plt.show()