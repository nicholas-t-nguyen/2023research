import numpy as np
from stochastic import brownian_motion
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 6))

t = 10
steps = 10000000
x = brownian_motion(t ,steps)
y = brownian_motion(t ,steps)

t_eval = np.linspace(0, t, steps + 1)

plt.plot(t_eval, y)
plt.xlim(0)
plt.xlabel('t')
plt.ylabel('Bt')

plt.show()

