import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t):
x    dxdt = -1*z[0]
    dydt = -1*z[1]
    dzdt = [dxdt,dydt]
    return dzdt

# initial condition
z0 = [0.3,0.5]

# time points
t = np.linspace(0,5)

# solve ODE
z = odeint(model,z0,t)
# plot results
plt.plot(t,z[:,0],'b-')
plt.plot(t,z[:,1],'r--')
plt.ylabel('response')
plt.xlabel('time')
# plt.legend(loc='best')
plt.show()