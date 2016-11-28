import math
import random
import matplotlib.pyplot as plt

sin = math.sin
cos = math.cos
pi = math.pi

def iadd(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def imult(a, b):
    return [a[0]*b[0] - a[1]*b[1], a[1]*b[0] + a[0]*b[1]]

def iswhole(n):
    return math.floor(n) == math.ceil(n) == n

def fft(x):
    assert iswhole(math.log(len(x), 2))
    if len(x) == 1:
        return [[x[0], 0]]
    X_beg = []
    X_end = []
    # recursively get the FFT of the even and then odd samples
    X_0_n2 = fft([x[m] for m in range(0, len(x), 2)])
    X_1_n2 = fft([x[l] for l in range(1, len(x), 2)])
    for k in range(len(x)//2):
        exponent = -2*pi*k/len(x)
        WX_term = imult([cos(exponent), sin(exponent)], X_1_n2[k])
        X_beg.append(iadd(X_0_n2[k], WX_term))
        X_end.append(iadd(X_0_n2[k], [-WX_term[0], -WX_term[1]]))
    return X_beg + X_end#

def imagnitude(a):
    return math.sqrt(a[0]**2 + a[1]**2)

#+random.uniform(0, 0.2)
x = [sin(2*pi*x_val/5)+5*sin(2*pi*x_val/40) for x_val in range(1024)]
X = fft(x)
X = X[:len(X)//2]
real = [imagnitude(a) for a in X]

plt.plot(real)
plt.show()



