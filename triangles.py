import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if x < 0 or x > 1:
        return 0
    else:
        return 1 - x

def g(x):
    if x < 0 or x > 2:
        return 0
    else:
        return 1 - x/2

def riemann(f, g, bounds = [-3, 4], delta_x = 0.001):
    s = 0
    for x in np.arange(bounds[0], bounds[1], delta_x):
        s += f(x) * g(x) * delta_x
    return s

def convo(f, g, delta_u = 0.001):
    h = []
    for u in np.arange(-5, 5, delta_u):
        print(u)
        h.append(riemann(f, lambda y: g(u - y)))

    return h



h = convo(f, g)

plt.plot(np.arange(-5, 5, 0.001), h)
plt.show()

