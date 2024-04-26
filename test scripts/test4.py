from firsthittingtime import fht1cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp
import multiprocessing
import inspect
import csv

def dh_dt_zerodriver(t, h):
    return -2 / h

t = 6.25
steps = 100
dt = t / steps
t_span = [0, t]
t_eval = np.arange(0, t + dt, dt)

h0 = 5

sol = solve_ivp(dh_dt_zerodriver, t_span=t_span, y0=[h0], t_eval=t_eval)
interp = interp1d(t_eval, sol.y[0])
print(interp(6.25))
print(len(t_eval))
print(sol.y[0])

plt.figure(figsize=(8, 6), dpi=400)

zerodriver = lambda t: 0 * t

solinterp = interp1d(t_eval, sol.y[0])
fhtv, fhtl = fht1cc(solinterp, zerodriver, t, dt)

plt.plot(t_eval, [solinterp(t) for t in t_eval], color='black')
plt.plot(t_eval, [zerodriver(t) for t in t_eval], color='gold')
plt.scatter(fhtv, solinterp(fhtv), color='blue')
# plt.xlim((fhtv-0.1, fhtv+0.1))
# plt.ylim((solinterp(fhtv)-1, solinterp(fhtv)+1))
print(fhtv)
plt.show()
plt.close()
