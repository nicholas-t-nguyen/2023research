import sys
import matplotlib.pyplot as plt, mpld3
from multiprocessing import Pool, cpu_count
import numpy as np
from scipy.integrate import solve_ivp

def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))

def solve_diffeq_1cc(h0, t, lambda1):
    event1cc.terminal = True
    event1cc.direction = 0
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=event1cc, rtol=1e-6, atol=1e-9)
    return sol

def event1cc(t, h, lambda1):
    return h[0] - lambda1(t)

def mainfunc(h0):
    lambda1 = lambda t: t * 0
    t = 10000000000
    sol = solve_diffeq_1cc(h0, t, lambda1)
    fht = sol.t[-1]
    return fht, sol

#zero driver plots various h0
if __name__ == "__main__":
    # print(cpu_count())
    # print(sys.executable)
    # print(sys.version)
    # print(sys.version_info)

    harr = np.arange(-10, 10.1, 0.1)
    T_values = []

    pool = Pool()
    T_values = pool.map(mainfunc, harr)
    pool.close()
    pool.join()

    fhts = [values[0] for values in T_values]

    A_values = []
    for i in range(len(harr)):
        delta = fhts[i] - ((harr[i] ** 2)/4)
        A_values.append(delta)

    plt.figure(figsize=(8, 6), dpi=200)
    for h, T in zip(harr, fhts):
        if T == 10000000000:
            plt.plot(h, 0, 'o', color='red')
            print(f"{h} failed")
        else:
            plt.plot(h, T, 'o', color='black')
    plt.xlabel("$h_0$")
    plt.ylabel("FHT")
    plt.savefig('paperpics/1a zero-driver fhts.png')
    plt.close()

    plt.figure(figsize=(8, 6), dpi=200)
    plt.scatter(harr, A_values, color='black')
    plt.xlabel("$h_0$")
    plt.ylabel("Error")
    plt.savefig('paperpics/1b zero-driver errors.png')
    plt.close()

    plt.figure(figsize=(8, 6), dpi=200)
    maxfht = max(fhts)

    t_valuesext = np.arange(0, maxfht * 1.1, 0.00001)

    driver = lambda t: 0 * t
    i = 0
    for h0, sol in zip(harr, T_values):
        fht = sol[0]
        solution = sol[1]
        t_values = np.arange(0, fht, 0.00001)
        plt.plot(solution.t, solution.y[0], color='black')
        plt.plot(t_valuesext, [driver(t) for t in t_valuesext], color='#CFB87C')
        i += 1
        print(i)

    plt.xlabel("time")
    plt.ylabel("y")
    plt.savefig('paperpics/1c zero-driver drivers + sols.png')

    #OR

    # fig, axs = plt.subplots(2, figsize=(8, 12), dpi=400)
    #
    # # Plotting the first subplot with harr and T_values
    # axs[0].plot(harr, T_values, 'o', color='blue')
    # axs[0].set_title("λ(t) = 0")
    # axs[0].set_xlabel("h0")
    # axs[0].set_ylabel("fht")
    #
    # # Plotting the second subplot with harr and A_values
    # axs[1].scatter(harr, A_values, color='red')
    # axs[1].set_title("error between numerical and analytical solution for each h0")
    # axs[1].set_xlabel("harr")
    # axs[1].set_ylabel("A_values")
    #
    # plt.tight_layout()
    # plt.safefig("1. ")
    # plt.close()