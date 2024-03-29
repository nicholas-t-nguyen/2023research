import numpy

from one_curve_case import solve_diffeq_scaled
import numpy as np
from matplotlib import pyplot as plt
from stochastic import brownian_motion
from scipy.interpolate import interp1d
from scipy.optimize import brentq as root

t = 1
steps = 1000
ss = t/steps
t_eval = np.arange(0, t+ss, ss)
kappa = 1
alpha = 10

fun = lambda x: 100 * x

plt.figure(figsize=(8, 6))

x = []
y= []

#bmv = brownian_motion(t, steps)
#bm = interp1d(t_eval, bmv)
#for alpha in numpy.linspace(0, 10, 1001):
sol = solve_diffeq_scaled(t, steps, 10, kappa, fun, alpha)
solinterp = interp1d(t_eval, sol.y[0])

lambdafun = lambda t, alpha=alpha: np.sqrt(kappa) * fun(t) + alpha * t
rootfun = lambda t, alpha=alpha: lambdafun(t) - solinterp(t)

fht = root(rootfun, a=0, b=1)
print(fht)
x.append(fht)
y.append(lambdafun(fht))

plt.show()

plt.plot(sol.t, sol.y[0])
plt.plot(t_eval, [lambdafun(t) for t in t_eval], color='brown')
plt.scatter(x, y, color='red')

plt.xlabel('t')
plt.ylabel('fht')

plt.savefig("fht/100x.png")
plt.show()