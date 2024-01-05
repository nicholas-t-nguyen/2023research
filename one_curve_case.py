import numpy as np
from scipy.integrate import solve_ivp

def scaled_dh_dt(t, h, kappa, stochastic, alpha):
    return (-2)/(h - (np.sqrt(kappa) * stochastic(t) + alpha * t))

def solve_diffeq_scaled(t, steps, h0, kappa, stochastic, alpha):
    t_span = [0, t]
    t_eval = np.linspace(0, t, steps + 1)
    sol = solve_ivp(scaled_dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(kappa, stochastic, alpha))
    return sol