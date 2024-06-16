import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from multiprocessing import Pool, cpu_count
import inspect
import csv
import numpy as np
from scipy.integrate import solve_ivp

def dh_dt_1cc(t, h, lambda1):
    return (-2) / (h - (lambda1(t)))

def solve_diffeq_1cc(h0, t, lambda1):
    event1cc.terminal = True
    event1cc.direction = 0
    sol = solve_ivp(dh_dt_1cc, t_span=[0, t], y0=[h0], args=(lambda1,), events=event1cc, rtol=1e-6, atol=1e-9, dense_output=True)
    return sol

def event1cc(t, h, lambda1):
    return h[0] - lambda1(t)

def mainfunc(h0):
    lambda1 = lambda t: t
    t = 10000000000
    sol = solve_diffeq_1cc(h0, t, lambda1)
    fht = sol.t[-1]
    return fht, sol

#shadow generating solution and driver plot with varying h0
if __name__ == "__main__":
    gold15 = ["CFB87C","D1BA80","D2BD85","D4BF89","D6C28E","D7C492","D9C697","DBC99B","DCCBA0","DECDA4","E0D0A8","E1D2AD","E3D5B1","E5D7B6","E6D9BA","E8DCBF","E9DEC3","EBE0C8","EDE3CC","EEE5D1","F0E8D5","F2EAD9","F3ECDE","F5EFE2","F7F1E7","F8F3EB","FAF6F0","FCF8F4","FDFBF9","FFFDFD"]
    black15 = ["000000","090909","121111","1A1A1A","232323","2C2C2C","353434","3E3D3D","464646","4F4F4F","585757","616060","6A6969","727171","7B7A7A","848383","8D8C8C","959494","9E9D9D","A7A6A6","B0AEAE","B9B7B7","C1C0C0","CAC9C9","D3D1D1","DCDADA","E5E3E3","EDECEC","F6F4F4","FFFDFD"]

    harr = np.arange(-1, 1.1, 0.1)
    T_values = []

    pool = Pool()
    T_values = pool.map(mainfunc, harr)
    pool.close()
    pool.join()

    fhts = [values[0] for values in T_values]
    maxfht = max(fhts)
    # print(T_values[1])
    t_valuesext = np.arange(0, maxfht * 1.1, 0.00001)
    plt.figure(figsize=(8, 6), dpi=200)

    for h0, sol, gold, black in zip(harr, T_values, gold15, black15):
        fht = sol[0]
        solution = sol[1]
        t_values = np.arange(0, fht, 0.00001)
        driver = lambda t: t
        plt.plot(t_values, [solution.sol(t) for t in t_values], color=f"#{black}")
        plt.plot(t_valuesext, [driver(t) for t in t_valuesext], color=f"#{gold}")
    plt.savefig("testewateaw.png")

    plt.figure(figsize=(8, 6), dpi=200)
    plt.scatter(harr, fhts)
    plt.savefig("testewateaw1.png")