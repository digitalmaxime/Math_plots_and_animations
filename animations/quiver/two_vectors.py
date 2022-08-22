import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# X, Y = np.meshgrid(np.linspace(0, 10), np.linspace(0, 10))
# X, Y = ([0, 1, 2], [1, 1, 1])
X, Y = (0, 0)
fig, ax = plt.subplots()
# Q = ax.quiver(X, Y , 1, 1)
Q = plt.quiver(X, Y, 1, 1)
Q2 = plt.quiver(1, 1, -1, -1)
# plt.draw()
# plt.pause(2)
# Q.set_offsets(Q.get_offsets() * np.array([1, .5]))
# Q.set_offsets([1, 1, 1])
# plt.draw()

def update_quiver(num, Q):
    Q.set_offsets(Q.get_offsets() + np.array([1/10000, .5/10000]))
    # Q.set_UVC(U,V, C=V)

anim = FuncAnimation(fig, update_quiver, fargs=(Q,), interval=50, blit=False)

plt.show()