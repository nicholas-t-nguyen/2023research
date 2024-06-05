import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq as root
from matplotlib import pyplot as plt

def dh_dt_1cc(t, h):
    return (-1) / (2 * np.sqrt(-1 * t))

def solve_diffeq_1cc(t, h0):
    t_span = [0, t]
    sol = solve_ivp(dh_dt_1cc, t_span=t_span, y0=h0, dense_output=True,  rtol=1e-5, atol=1e-9, max_step=1e-6)
    return sol

def fht1cc(sol, lambda1, t, dt):
    x_t = np.arange(0, t + dt, dt)
    rootfun1 = lambda t: sol(t) - lambda1(t)

    b = 0
    for i in range(len(x_t)):
        p1 = rootfun1(x_t[i]) * rootfun1(x_t[i + 1])
        if p1 <= 0:
            b = x_t[i+1]
            break

    fhtv = root(rootfun1, 0, b)

    return fhtv

if __name__ == "__main__":
    plt.figure(figsize=(8, 6), dpi=800)

    t = 2
    h0 = [complex(2)]

    sol = solve_diffeq_1cc(t, h0)
    print(sol)

    # try:
    #     fhtv = fht1cc(sol.sol.real, lambda1, t, dt)
    # except:
    #     print("failed fht")

    print('cont')
    t_dense = sol.t
    y_dense = sol.y[0]
    print(sol.sol(t_dense).imag)
    print(sol.sol(t_dense))

    plt.scatter(sol.sol(t_dense).real[0],sol.sol(t_dense).imag[0])
    # plt.plot(t_dense, y_dense, color='black', label='Real part')
    # plt.plot(t_dense, sol.sol(t_dense).imag[0], color='red', label='Imaginary part')
    # plt.plot(sol.t, [lambda1(t) for t in sol.t], color='gold', label='Lambda1')
    # try:
    #     # plt.scatter(fhtv, sol.sol(fhtv), color='blue', label='First hitting time')
    # except:
    #     print("cont")

    # plt.xlim((0.0745, 0.0747))
    # plt.ylim((1.5, 1.6))

    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.title('Real and Imaginary Parts of the Solution')
    plt.legend()
    plt.show()
    plt.close()