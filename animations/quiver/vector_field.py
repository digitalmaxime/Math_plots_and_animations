import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MathOps.matrix_operation import matrix_vector_mul
from MathOps.matrix import Matrix

x_pos = np.arange(-np.pi*2, np.pi*2, 0.4)
y_pos = np.zeros(32)
# y_pos = np.arange(0, 2.2, 0.2)
U = 0
V = np.cos(x_pos)
# X, Y = np.meshgrid(x_pos, y_pos)
# U = np.cos(X)*Y
# V = np.sin(Y)*Y

print(x_pos)
print("*"*40)

fig, ax = plt.subplots()
# ax.quiver(X, Y, U, V, scale=5)
Q = ax.quiver(x_pos, y_pos, U, V)
# ax.xaxis.set_ticks([])
# ax.yaxis.set_ticks([])
# ax.set_aspect('equal')

ax.axis([-5, 5, -5, 5])

def update_quiver(num, Q, X, Y):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    U = 0
    V = np.cos(X + num*0.1)

    Q.set_UVC(U,V, C=V)
    return Q,

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
anim = FuncAnimation(fig, update_quiver, fargs=(Q, x_pos, y_pos),
                               interval=50, blit=False)
# fig.tight_layout()
plt.show()