import numpy as np
import matplotlib.pyplot as plt

start_accel = 20 # meter per sekund
vinkel = 60 # Grader
g = 9.8066 # meter per sekund i andre
time = np.linspace(0, 3.5, int(3.5*100))

def s(x, y, z):
    return np.cos(z*np.pi/180)*y*x

def h(t, v_0, alpha):
    return np.sin(alpha*np.pi/180)*v_0*t-(1/2)*g*t**2

plt.plot(s(time, start_accel, vinkel), h(time, start_accel, vinkel))
plt.show()