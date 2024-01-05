import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def brownian_motion(t, steps):
    dt = t / steps
    sd = np.sqrt(dt)
    array = np.random.normal(0, sd, steps)
    array = np.concatenate([[0], array])
    array = np.cumsum(array)
    return array

# Parameters
t_total = 1.0
num_steps = 100
t_eval = np.linspace(0, t_total, num_steps + 1)

# Generate Brownian motion
bmv = brownian_motion(t_total, num_steps)

# Create an interpolation function using interp1d
bm_interp = interp1d(t_eval, bmv, kind='linear')

# Generate points for the interpolation
t_interp = np.linspace(0, t_total, 1000)
bm_values_interp = bm_interp(t_interp)

# Plot the original Brownian motion and the interpolated curve
plt.plot(t_eval, bmv, 'o-', label='Brownian Motion')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Interpolated Brownian Motion')
plt.show()