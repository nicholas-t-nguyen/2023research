import numpy as np
from scipy.optimize import brentq as root
def fht2cc(sol, lambda1, lambda2, t, dt):
    x_t = np.arange(0, t + dt, dt)
    rootfun1 = lambda t: sol(t) - lambda1(t)
    rootfun2 = lambda t: sol(t) - lambda2(t)
    b = 0
    for i in range(len(x_t)):
        p1 = rootfun1(x_t[i]) * rootfun1(x_t[i + 1])
        p2 = rootfun2(x_t[i]) * rootfun2(x_t[i + 1])
        if p1 <= 0 or p2 <= 0:
            b = x_t[i+1]
            break
    try:
        sol = root(rootfun1, 0, b)
    except:
        sol = root(rootfun2, 0, b)
    return sol

if __name__ == "__main__":
    sol = lambda n: -3 * n + 2
    lambda1 = lambda n: 2 * n ** 2 + 1
    lambda2 = lambda n: -0.5 * n + 1.5
    print(fht2cc(sol, lambda1, lambda2, 10, 0.01))
