import numpy as np

def random_walk(t, steps):
    dt = t / steps
    step_set = [-dt, dt]
    array = np.random.choice(step_set, size=steps)
    array = np.concatenate([[0], array])
    array = np.cumsum(array)
    return array

def brownian_motion(t, steps):
    dt = t / steps
    sd = np.sqrt(dt)
    array = np.random.normal(0, sd, steps)
    array = np.concatenate([[0], array])
    array = np.cumsum(array)
    return array

def brownian_motion_nd(dimensions, t, steps):
    array = brownian_motion(t, steps)
    for i in range(dimensions - 1):
        array = np.vstack([array, brownian_motion(t, steps)])
    return array

def bessel_process(dimensions, t, steps):
    return np.linalg.norm(brownian_motion_nd(dimensions, t, steps), axis=0)

if __name__ == '__main__':
    print(random_walk(1, 10))