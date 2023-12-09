import numpy as np

def brownian_motion(steps, dimensions):
    array = np.random.normal(0, 1, steps)
    for i in (range(dimensions - 1)):
        temp = np.random.normal(0, 1 , steps)
        array = np.vstack([array, temp])
    cumsumarray = np.cumsum(array, axis=1)
    return cumsumarray

def bessel_process(steps, dimensions):
    return np.linalg.norm(brownian_motion(steps, dimensions), axis=0)
