from stochastic import brownian_motion
from diffeq import solve_diffeq
from scipy.interpolate import interp1d
import numpy as np
from scipy.integrate import solve_ivp

def scaled_dh_dt(t, h, stochastic, kappa, alpha):
    return (-2)/(h - (np.sqrt(kappa) * stochastic(t) + alpha * t))

def solve_diffeq_scaled(t, steps, h0, kappa, alpha):
    t_span = [0, t]
    t_eval = np.linspace(0, t, steps + 1)

    bm = brownian_motion(t, steps)
    brownian = interp1d(x=t_eval, y=bm)

    sol = solve_ivp(scaled_dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(brownian, kappa, alpha))
    return sol