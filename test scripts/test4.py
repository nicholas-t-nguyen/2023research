import matplotlib.pyplot as plt
import numpy as np
from sympy import latex, symbols, sqrt
import os
from scipy.integrate import solve_ivp

def dh_dt(t, h, lambda1, lambda2):
    return (1 / 2) * (((-2) / (h - (lambda1(t)))) + ((-2) / (h + (lambda2(t)))))

def solve_diffeq(t, steps, h0, lambda1, lambda2):
    t_span = [0, t]
    t_eval = np.linspace(0, t, steps)
    sol = solve_ivp(dh_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(lambda1, lambda2))
    return sol

h0_values = np.arange(-1, 1.1, 0.1)
h0_values = h0_values[h0_values != 0]
steps = 10000
t = 5

t_sym, x = symbols('t x')
lambda1 = lambda t: sqrt(t)
lambda2 = lambda t: sqrt(t)

plt.figure(figsize=(8, 6))

for h0 in h0_values:
    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)
    plt.plot(sol.t, sol.y[0], label=f'x={h0}')

lambda1_str = str(lambda1(t_sym)).replace('**', '^')
lambda1_latex = latex(lambda1(t_sym))

plt.xlabel('t')
plt.ylabel('h(t)')
#plt.ylim(-25, 25)

title = f'Solution of $\\frac{{dh}}{{dt}}$ with all values of $h_0$ at $t=0$ with $\\lambda_{{1,2}}(t) = {lambda1_latex}$'
plt.title(title)

file_path = f'plots/deterministic/e^x/{lambda1_str}/all_values.png'
#directory = os.path.dirname(file_path)
#if not os.path.exists(directory):
#    os.makedirs(directory)

# plt.savefig(file_path)  # Save the plot with all values
