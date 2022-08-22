import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MathOps.matrix_operation import matrix_vector_mul
x_data = []
y_data = []

"""
    class matplotlib.animation.FuncAnimation(
        fig, func, frames=None
        (optionnal) interval (time in ms between each frame, default val=200)
    )
"""
fig = plt.figure()
ax = plt.axes(xlim=(-4,4), ylim=(-4, 4))
# ax = plt.axes()
line, = ax.plot([],[], lw=3)

def init() :
    line.set_data([],[])
    return line,

def animate(i):
    x = np.linspace(-4, 4, 1000)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    y = np.sin(i * x/100)
    line.set_data(x, y)
    return line, 

if __name__ == "__main__" :
    anim = FuncAnimation(fig, animate, frames=100, init_func=init, interval=20, blit=True)

    #anim.save('./sine_wave.gif', writer='imagemagick')

    # def animation_frame2(i) :
    #     x_data.append(i)
    #     y_data.append(np.sin(i))

    #     line.set_xdata(x_data)
    #     line.set_ydata(y_data)
    #     return line,

    # animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(-10, 10, 0.5), interval=10)
    plt.show()