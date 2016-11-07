import numpy as np
from math import exp
from random import randint, seed
import matplotlib.pyplot as plt

seed(0)

# steps are in 0.001
step_size = 0.001

f_func = lambda x: 0 if (x < -2 or x > 2) else exp(-x**2)

x = -2
f = {}
f_array = []
for i in range(401):
    f[x] = f_func(x)
    f_array.append(f_func(x))
    x += 0.01

# generate a randomish g() function that we want to smooth
x = -10
old_val = 0
g = {}
g_array = []
for i in range(20001):
    delta = randint(-3, 3)
    current_val = old_val + delta
    g[x] = current_val
    g_array.append(current_val)
    old_val = current_val

    x += step_size


def convo(f, g):
    h = []
    h_len = len(f) + len(g) - 1

    for i in range(1, h_len+1):
        h.append(0)
        j_start = max(1 - len(g) + i, 1)
        j_end = min(len(f), i)
        j_delta = 1 - 2*(j_start > j_end) # whatever
        for j in range(j_start, j_end + j_delta, j_delta):
            k = i - j + 1
            h[-1] += f[j-1]*g[k-1]

        h[-1] /= abs(j_end - j_start) + 1
        h[-1] *= 2

    return h

h = convo(f_array, g_array)
plt.plot(g_array, )
x = np.arange(-(len(f)//2), len(g)+len(f)//2, 1)
plt.plot(x, h, lw=3)
plt.show()







    
