from numpy import *
import matplotlib.pyplot as plt
import numpy as np
x0 = 100
k=12
t=12
p = 5/k
N = t*12
x = zeros(N+1)
x[0] = x0
# for n in range(N+1)[1:]:
#     x[n] = x[n-1] + (p/100.0)*x[n-1]
# plt.plot(range(N+1), x)
# plt.xlabel("Lata")
# plt.ylabel("Kapitał")
# plt.xticks(range(0,N+t,t), range(t+1))
# plt.show()
def f(n):
    if n == 0:
        return x0
    else:
        return f(n - 1)*(1 + (p / 100.0))
print(f(12))
