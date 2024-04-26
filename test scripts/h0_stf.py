from diffeq import solve_diffeq_2cc
from firsthittingtime import fht2cc
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import multiprocessing
import inspect
import csv



print("Number of cpu : ", multiprocessing.cpu_count())

t = 500
steps = 5000000
dt = t / steps
t_eval = np.arange(0, t + dt, dt)
harr = np.arange(-1, 1.01, 0.01)

plt.figure(figsize=(8, 6), dpi=400)

lambda1 = lambda t: 2 * np.sqrt(t) + 0.01
lambda2 = lambda t: -2 * np.sqrt(t) - 0.01

def mainfunc(h0):
    sol = solve_diffeq_2cc(t, steps, h0, lambda1, lambda2)
    try:
        solinterp = interp1d(t_eval, sol.y[0])
    except:
        print(f"divide by zero error with h0 = {h0}")
        return h0, 0, 'red'

    try:
        fhtv, fhtl = fht2cc(solinterp, lambda1, lambda2, t, dt)
        if fhtl == 1:
            color = "blue"
        elif fhtl == 2:
            color = "orange"
        print(f"fht={fhtv} and h0={h0}")
        return h0, fhtv, color
    except:
        print(f"out of range at h0 = {h0}")
        return h0, 0, 'red'


if __name__ == "__main__":
    pool = multiprocessing.Pool()
    results = pool.imap(mainfunc, harr)
    pool.close()
    pool.join()

    ordered_results = list(results)

    h0_vals, fht_vals, colors = zip(*ordered_results)

    # Create a list of tuples representing rows in the CSV file
    data = list(zip(h0_vals, fht_vals, colors))

    # Define the filename for the CSV file
    lambda1_str = inspect.getsource(lambda1)
    lambda2_str = inspect.getsource(lambda2)

    csv_filenamepre = f"{lambda1_str}_{lambda2_str}_t={t}_steps={steps}_dt={dt}.csv"
    csv_filename = csv_filenamepre.replace(" ", "")
    # Write the data to the CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['h0', 'fht', 'color'])  # Write the header
        csv_writer.writerows(data)  # Write the data rows

    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath,amsfonts}'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.scatter(h0_vals, fht_vals, color=colors)
    title_str = r'FHT of different $h_0$ with $\lambda^1_t = 2\sqrt{t} + 0.01$ and $\lambda^2_t = -2\sqrt{t} - 0.01$'

    plt.title(title_str)
    plt.xlabel(r'$h_0$')
    plt.ylabel(r'FHT')
    plt.show()
    plt.close()

