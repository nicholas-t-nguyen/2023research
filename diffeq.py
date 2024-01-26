import numpy as np
from scipy.integrate import solve_ivp

def dh_dt(t, h, lambda1, lambda2):
    return (1 / 2) * (((-2) / (h + (lambda1(t)))) + ((-2) / (h - (lambda2(t)))))

def solve_diffeq(t, steps, h0, lambda1, lambda2):
    ss = t / steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(lambda1, lambda2))
    return sol