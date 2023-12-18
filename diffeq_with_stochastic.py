import numpy as np
from scipy.interpolate import interp1d
from diffeq import solve_diffeq
from stochastic import random_walk, brownian_motion

def diffeq_random_walk(t, steps, h0):
    t_eval = np.linspace(0, t, steps + 1)
    rw1 = random_walk(t, steps)
    lambda1 = interp1d(x=t_eval, y=rw1)

    rw2 = random_walk(t, steps)
    lambda2 = interp1d(x=t_eval, y=rw2)

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    return sol
def diffeq_brownian_motion(t, steps, h0):
    t_eval = np.linspace(0, t, steps + 1)
    b1 = brownian_motion(t, steps)
    lambda1 = interp1d(x=t_eval, y=b1)

    b2 = brownian_motion(t, steps)
    lambda2 = interp1d(x=t_eval, y=b2)

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    return sol


