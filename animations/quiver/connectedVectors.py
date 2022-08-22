import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MathOps.matrix import Matrix
from MathOps.matrix_operation import matrix_vector_mul

plt.subplots()
M = Matrix.m2by2
fig, ax = plt.subplots()
    
x_pos = [0, 0]
y_pos = [0, 0]

x_direct = [1, -1]
y_direct = [1, -1]
direction_vector = np.array((x_direct, y_direct))

Q = ax.quiver(x_pos,y_pos,x_direct,y_direct, scale=10)
ax.set_title('Example', fontsize = 14, fontweight ='bold')
#plt.axis([-30, 30, -30, 30])
ax.axis([-30, 30, -30, 30])

def init():
    # M = Matrix.m2by2
    U = direction_vector[0]
    V = direction_vector[1]
    Q.set_UVC(U,V)
    return Q,


def update_quiver(num, Q, X, Y):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """
    # matrix = np.array(
    #     [[1, num/100], 
    #     [0, 1]]
    # )
    # matrix = matrix * matrix
    # Vec = matrix_vector_mul(matrix, direction_vector)
    
    U = Vec[0]
    V = Vec[1]

    Q.set_UVC(U,V, C=U*V)

    return Q,

# you need to set blit=False, or the first set of arrows never gets
# cleared on subsequent frames
anim = FuncAnimation(fig, update_quiver, init_func=int ,fargs=(Q, x_pos, y_pos),
                               interval=10, blit=False)
# fig.tight_layout()
plt.show()