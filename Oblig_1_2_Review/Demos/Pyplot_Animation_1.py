import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

v_0 = 20 # meter per sekund
vinkel = 60 # Grader
g =9.8066 # meter per sekund i andre
t = np.linspace(0, 3.5, 101)

def s(t, v_0, alpha):
    s_verdier = np.cos(alpha*np.pi/180)*v_0*t
    return s_verdier
def h(t, v_0, alpha):
    h_verdier = np.sin(alpha*np.pi/180)*v_0*t-(1/2)*g*t**2
    return h_verdier

fig = plt.figure()
l, = plt.plot([], [])
plt.xlim(min(s(t, v_0, vinkel)), max(s(t, v_0, vinkel))+1)
plt.ylim(min(h(t, v_0, vinkel)), max(h(t, v_0, vinkel))+5)

writer = FFMpegWriter(fps=30)

xlist = []
ylist = []

with writer.saving(fig, 'throw_3c.mp4', 100):
    for time in t:
        xlist.append(s(time, v_0, vinkel))
        ylist.append(h(time, v_0, vinkel))

        l.set_data(xlist, ylist)
        l.set_label(f'Time: {time:.3f}\nHeight (m): {h(time, v_0, vinkel):.3f}\nDistance (m): {s(time, v_0, vinkel):.3f}')
        plt.legend()

        writer.grab_frame()
        
# Close the plot
plt.close()