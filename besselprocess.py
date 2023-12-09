import numpy as np

def brownian_motion(dimensions, steps, T):
    sd = np.sqrt(T / steps)
    array = np.random.normal(0, sd, steps)
    for i in (range(dimensions - 1)):
        temp = np.random.normal(0, sd, steps)
        array = np.vstack([array, temp])
    cumsumarray = np.cumsum(array, axis=1)
    return cumsumarray

def bessel_process(dimensions, steps, T):
    return np.linalg.norm(brownian_motion(dimensions, steps, T), axis=0)