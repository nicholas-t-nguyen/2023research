import matplotlib.pyplot as plt
import numpy as np
from diffeq import solve_diffeq

h0_values = [10]
steps = 10000000
t = 100

lambda1 = lambda t: t
lambda2 = lambda t: t

plt.figure(figsize=(8, 6))

if __name__ == '__main__':
    sol = solve_diffeq(t, steps, h0_values, lambda1, lambda2)
    min_value = np.min(sol.y[0])

    plt.xlabel('t')
    plt.ylabel('h(t)')
    plt.title('Solution of dh/dt for different x at t=0')
    plt.savefig('1.png')
    plt.show()