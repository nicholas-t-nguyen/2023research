import numpy as np
from scipy.integrate import solve_ivp

def scaled_dh_dt(t, h, kappa, fun, alpha):
    return (-2)/(h - (np.sqrt(kappa) * fun(t) + alpha * t))

def solve_diffeq_scaled(t, steps, h0, kappa, fun, alpha):
    ss = t/steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(scaled_dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(kappa, fun, alpha))
    return sol