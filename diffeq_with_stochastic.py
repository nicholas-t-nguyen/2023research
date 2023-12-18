import numpy as np
from scipy.interpolate import interp1d
from diffeq import solve_diffeq
from stochastic import brownian_motion

def diffeq_brownian_motion(t, steps, h0):
    t_eval = np.linspace(0, t, steps + 1)
    b1 = brownian_motion(t, steps)
    lambda1 = interp1d(x=t_eval, y=b1)

    b2 = brownian_motion(t, steps)
    lambda2 = interp1d(x=t_eval, y=b2)

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    return sol


