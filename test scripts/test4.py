import numpy as np
import matplotlib.pyplot as plt
from diffeq import fhtlambda1, fhtlambda2, solve_diffeq_2cc

# Define the differential equation dy/dt = -2/y - x
def dydt(y, x):
    return np.where(y > np.sqrt(x), -2/(y - x ** x), np.nan)

# Define the range of y and t values
y = np.linspace(0.1, 5, 20)
x = np.linspace(0, 5, 20)

# Create a meshgrid for y and t
Y, X = np.meshgrid(y, x)

# Calculate the direction field
DYDT = dydt(Y, X)

# Plot the direction field
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, np.ones_like(DYDT), DYDT, scale=20)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Direction Field for dy/dt = -2/y - x')
plt.grid(True)
plt.show()
