import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import latex, symbols, sqrt
import os
from diffeq import solve_diffeq

h0_values = [0.1]
steps = 1000
t = 1


lambda1 = lambda t: t
lambda2 = lambda t: sqrt(t)

for h0 in h0_values:
    plt.figure(figsize=(8, 6))

    # Assuming you have a correct implementation of solve_diffeq

    sol = solve_diffeq(t, steps, h0, lambda1, lambda2)

    plt.plot(sol.t, sol.y[0], label=f'x={h0}')
    t_sym, x = symbols('t x')
    lambda1_str = str(lambda1(t_sym)).replace('**', '^')
    lambda1_latex = latex(lambda1(t_sym))

    plt.xlabel('t')
    plt.ylabel('h(t)')

    # Set y-axis limits
   #  plt.ylim(-.001, .001)

    title = f'Solution of $\\frac{{dh}}{{dt}}$ for $h(t_0) = {h0}$ at $t=0$ with $\\lambda_{{1,2}}(t) = {lambda1_latex}$'

    plt.title(title)
    plt.show()

"""
    file_path = f'plots/deterministic/e^t/{lambda1_str}/x={h0}.png'
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(file_path)  # Save the plot with the modified expression
   """


