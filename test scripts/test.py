import numpy as np
from scipy.interpolate import interp1d
from diffeq import solve_diffeq
from stochastic import random_walk, brownian_motion
from matplotlib import pyplot as plt
from diffeq_with_stochastic import diffeq_random_walk

h0 = 10
t = 33
steps = 100
t_eval = np.linspace(0, t, steps + 1)

rw1 = brownian_motion(t, steps)
lambda1 = interp1d(x=t_eval, y=rw1)

rw2 = brownian_motion(t, steps)
lambda2 = interp1d(x=t_eval, y=rw2)

sol1 = solve_diffeq(t, steps, h0, lambda1, lambda2)
sol2 = solve_diffeq(t, steps, -h0, lambda1, lambda2)

def plot1():
    plt.figure(figsize=(8, 6))

    plt.plot(sol1.t, sol1.y[0], color='b')
    plt.plot(sol2.t, sol2.y[0], color='b')
    plt.plot(t_eval, rw1, color='r')
    plt.plot(t_eval, rw2, color='g')

    plt.xlabel('t')
    plt.ylabel('Bt')

    plt.show()


plot1()

##semi martingale one curve case


#multiple starting points