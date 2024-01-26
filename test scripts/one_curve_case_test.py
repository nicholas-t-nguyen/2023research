from one_curve_case import solve_diffeq_scaled
import numpy as np
from matplotlib import pyplot as plt
from stochastic import brownian_motion
from scipy.interpolate import interp1d

t = 100
steps = 1000
t_eval = np.linspace(0, t, steps + 1)
kappa = 10
alpha = 1

plt.figure(figsize=(8, 6))

bmv = brownian_motion(t, steps)
bm = interp1d(t_eval, bmv)

sol = solve_diffeq_scaled(t, steps, 10, kappa, bm, alpha)
plt.plot(sol.t, sol.y[0])

plt.xlabel('t')
plt.ylabel('Bt')

plt.show()