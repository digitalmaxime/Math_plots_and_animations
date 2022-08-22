import matplotlib.pyplot as plt
import numpy as np
import random
x_values = []
y_values = []
ax = plt.axes(xlim=(-4,4), ylim=(-4, 4))
line, = ax.plot([],[], lw=3)

# for _ in range(10): 
#     x_values.append(random.randint(0, 100))
#     y_values.append(random.randint(0, 100))

#     plt.xlim(0, 100)
#     plt.ylim(0, 100)
#     plt.scatter(x_values, y_values, color="black")
#     plt.pause(0.01)
for i in range(100):
    # x = np.linspace(-4, 4, 1000)
    # y = np.sin(i*x/100)
    x_values.append(i)
    y_values.append(50 + np.sin(i / np.pi) * 40)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    # y_values.append(y)
    plt.plot(x_values, y_values)
    plt.pause(0.0001)
plt.show()
