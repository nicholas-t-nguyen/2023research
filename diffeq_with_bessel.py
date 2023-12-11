import numpy as np
from scipy.interpolate import interp1d
from besselprocess import bessel_process
from diffeq import solve_diffeq
def diffeq_bessel(num_simulations, t, steps, h0_values):
    t_eval = np.linspace(0, t, steps)
    for i in range(num_simulations):
        b1_value = bessel_process(2, t, steps)
        lambda1 = interp1d(x=t_eval, y=b1_value)

        b2_value = bessel_process(2, t, steps)
        lambda2 = interp1d(x=t_eval, y=b2_value)

        solve_diffeq(t, steps, h0_values, lambda1, lambda2)

