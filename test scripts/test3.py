import numpy
from diffeq import solve_diffeq_three_curve
import numpy as np
from matplotlib import pyplot as plt
from stochastic import brownian_motion
from scipy.interpolate import interp1d
from scipy.optimize import brentq as root
from PIL import Image, ImageDraw

t = 10
steps = 100000
ss = t/steps
t_eval = np.arange(0, t+ss, ss)
kappa = 1
alpha = 1
harr = [5]
h0 = 5.1

lambda1 = lambda x: -x
lambda2 = lambda x: np.sqrt(x) + 2
lambda3 = lambda x: x + 1

#bmv = brownian_motion(t, steps)
#bm = interp1d(t_eval, bmv)

plt.figure(figsize=(8, 6), dpi=400)
x = []
y = []

for h0 in harr:
    sol = solve_diffeq_three_curve(t, steps, h0, lambda1, lambda2, lambda3)
    solinterp = interp1d(t_eval, sol.y[0])

    rootfun2 = lambda t: lambda2(t) - solinterp(t)

    fht = root(rootfun2, a=0, b=3.7)
    print(fht)
    x.append(fht)
    y.append(lambda2(fht))

    plt.plot(sol.t, sol.y[0], color='black')
    plt.scatter(x, y)

plt.plot(t_eval, [lambda1(t) for t in t_eval], color='red')
plt.plot(t_eval, [lambda2(t) for t in t_eval], color='green')
plt.plot(t_eval, [lambda3(t) for t in t_eval], color='blue')


#plt.scatter(x, y)

plt.xlabel(f'test')
plt.ylabel('x value of fht')

#plt.xlim(0, 100)
#plt.ylim(6, 14.5)

img_filename = f"fht/fhtgif/frame_{kappa:.2f}.png"
plt.show()
plt.close()



