import numpy as np
from scipy.integrate import solve_ivp

def dh_dt_zerodriver(t, h):
    return -2 / h

def solve_diffeq_zerodriver(t, steps, h0):
    ss = t / steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(dh_dt_zerodriver, t_span=t_span, y0=[h0], t_eval=t_eval)
    return sol

def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))

def solve_diffeq_1cc(t, steps, h0, lambda1):
    ss = t / steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(dh_dt_1cc, t_span=t_span, y0=[h0], t_eval=t_eval, args=(lambda1,))
    return sol

def dh_dt_2cc(t, h, lambda1, lambda2):
    return (1 / 2) * (((-2) / (h - (lambda1(t)))) + ((-2) / (h - (lambda2(t)))))

def solve_diffeq_2cc(t, steps, h0, lambda1, lambda2):
    ss = t / steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(dh_dt_2cc, t_span=t_span, y0=[h0], t_eval=t_eval, args=(lambda1, lambda2), method='BDF')
    return sol

def dh_dt_3cc(t, h, lambda1, lambda2, lambda3):
    return (1 / 3) * (((-2) / (h - (lambda1(t)))) + ((-2) / (h - (lambda2(t)))) + ((-2) / (h - (lambda3(t)))))

def solve_diffeq_3cc(t, steps, h0, lambda1, lambda2, lambda3):
    ss = t / steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(dh_dt_3cc, t_span=t_span, y0=[h0], t_eval=t_eval, args=(lambda1, lambda2, lambda3))
    return sol

def scaled_dh_dt(t, h, kappa, fun, alpha):
    return (-2)/(h - (np.sqrt(kappa) * fun(t) + alpha * t))

def solve_diffeq_scaled(t, steps, h0, kappa, fun, alpha):
    ss = t/steps
    t_span = [0, t]
    t_eval = np.arange(0, t + ss, ss)
    sol = solve_ivp(scaled_dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(kappa, fun, alpha))
    return sol

##remove behavior after fht
##get accurate fht
##check continuity