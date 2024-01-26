import numpy as np
from scipy.interpolate import interp1d
from diffeq import solve_diffeq
from stochastic import random_walk, brownian_motion

def solve_diffeq_random_walk(t, steps, h0):
    ss = t/steps
    t_eval = np.arange(0, t + ss, ss)
    rw1 = random_walk(t, steps)
    lambda1 = interp1d(x=t_eval, y=rw1)

    rw2 = random_walk(t, steps)
    lambda2 = interp1d(x=t_eval, y=rw2)

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    return sol

def solve_diffeq_brownian_motion(t, steps, h0):
    ss = t/steps
    t_eval = np.arange(0, t + ss, ss)
    b1 = brownian_motion(t, steps)
    lambda1 = interp1d(x=t_eval, y=b1)

    b2 = brownian_motion(t, steps)
    lambda2 = interp1d(x=t_eval, y=b2)

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    return sol


