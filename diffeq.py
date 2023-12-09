import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def d_h_dt(t, h):
    return (1 / 2) * (((-2) / (h - (np.sqrt(t)))) + ((-2) / (h  + (np.sqrt(t)))))


h0_values = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]  # You can customize this list with the values of x you want to test

t_eval = np.linspace(0, 10, 50000)

plt.figure(figsize=(8, 6))

for h0 in h0_values:
    sol = solve_ivp(d_h_dt, [0, 10], [h0], t_eval=t_eval)

    plt.plot(sol.t, sol.y[0], label=f'x={h0}')

plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Solution of dh/dt for different x at t=0')
plt.savefig('1.png')
plt.show()

