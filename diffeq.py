import numpy as np
from scipy.integrate import solve_ivp

def fhtlambda1(t, h, lambda1):
    return h[0] - lambda1(t)

def fhtlambda2(t, h, lambda2):
    return h[0] - lambda2(t)

def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))

def solve_diffeq_1cc(h0, t, lambda1):
    fhtlambda1.terminal = True
    fhtlambda1.direction = 0
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=fhtlambda1, rtol=1e-6, atol=1e-9)
    return sol

def dh_dt_2cc(t, h, lambda1, lambda2):
    return (1 / 2) * (((-2) / (h - (lambda1(t)))) + ((-2) / (h - (lambda2(t)))))

def solve_diffeq_2cc(h0, t, lambda1, lambda2):
    fhtlambda1.terminal = True
    fhtlambda1.direction = 0
    fhtlambda2.terminal = True
    fhtlambda2.direction = 0

    sol = solve_ivp(dh_dt_2cc, t_span=[0, t], y0=[h0], args=(lambda1, lambda2), events=(fhtlambda1, fhtlambda2), rtol=1e-6, atol=1e-9)
    return sol


##remove behavior after fht
##get accurate fht
##check continuity