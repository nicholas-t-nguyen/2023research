import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

def d_h_dt(t, h, b1, b2):
    coefficient = 1 / 2
    return coefficient * ((-2) / (h - b1(t)) + (-2) / (h + b2(t)))

def brownian_motion(dimensions, steps, T):
    sd = np.sqrt(T / steps)
    array = np.random.normal(0, sd, (dimensions, steps))
    cumsumarray = np.cumsum(array, axis=1)
    return cumsumarray

def bessel_process(dimensions, steps, T):
    return np.linalg.norm(brownian_motion(dimensions, steps, T), axis=0)

# Parameters
h0_values = np.arange(10)  # Initial conditions for h
num_simulations = 100  # Number of simulations to run
steps = 10000
T = 100
t_span = [0, T]
t_eval = np.linspace(0, T, steps)

plt.figure(figsize=(8, 6))

for _ in range(num_simulations):
    # Generate Bessel process
    b1_value = bessel_process(2, steps, T)
    b1 = interp1d(x=t_eval, y=b1_value)

    b2_value = bessel_process(2, steps, T)
    b2 = interp1d(x=t_eval, y=b1_value)

    for h0 in h0_values:
        # Solve the differential equation
        sol = solve_ivp(d_h_dt, t_span=t_span, y0=[h0], t_eval=t_eval, args=(b1, b2))

        # Plot the solution
        plt.plot(sol.t, sol.y[0], label=f'x={h0}')

plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Solution of dh/dt for with Bessel process at t=0')
plt.savefig('2.png')
plt.show()