import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

g = 9.8066
t = np.linspace(0, 3.0, 101)
v_0 = 20

def s(t, alpha):
    return np.cos(alpha * np.pi / 180) * v_0 * t

def h(t, alpha):
    h = np.sin(alpha * np.pi / 180) * v_0 * t - (1/2) * g * t**2
    return h

fig = plt.figure(figsize=(15,30))
plt.subplots_adjust(hspace=0.5)
lines = []

plots = []

for alpha in range(5, 50, 5):
    ax = fig.add_subplot(9, 1, alpha//5)
    plots.append(ax)
    ax.set_title(f'Degrees: {alpha}', fontweight ="bold")
    ax.set_xlim(0, 45)
    ax.set_ylim(0, max(h(t, alpha))+1)
    line, = plt.plot([], [], label=f'Angle: {alpha} degrees')
    lines.append(line)

writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)

# Initialize empty lists to store data for each angle
data = {alpha: {'x': [], 'y': []} for alpha in range(5, 90, 5)}

with writer.saving(fig, './throw.mp4', 100):
    for alpha in range(5, 50, 5):
        height = 0
        for time in t:
            x = s(time, alpha)
            y = h(time, alpha)
            
            # Append the data to the lists for the current angle
            data[alpha]['x'].append(x)
            data[alpha]['y'].append(y)
            
            index = (alpha - 5) // 5  # Calculate the index for the lines list
            lines[index].set_data(data[alpha]['x'], data[alpha]['y'])

            if y >= 0:
                if y >= height:
                    height = y
                lines[index].set_label(f'Time: {time:.3f}\nDistance (m): {x:.3f}\nHeight (m): {height:.3f}')
            plots[index].legend()

            writer.grab_frame()
        
# Close the plot
plt.close()