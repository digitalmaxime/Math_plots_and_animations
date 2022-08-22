import matplotlib.pyplot as plt
import numpy as np

# a = np.arange(6) # + 1j*np.arange(6) # returns dnarray
# #a = np.array([1, 2, 3, 4, 5, 6])    # returns ndarray
# a = np.append(a, np.array([11, 12, 13]))
# print(a)
# b = [111, 222, 333]
# c = np.concatenate((a, b))
# print(c)
# d = [666, 13, 'the devil'] # np will interprete all as strings
# e = np.append(c, d)
# print('-' * 20)
# print(e)

# print("--")
# fig,ax = plt.subplots()
# ax.scatter(arr.real,arr.imag)
# #plt.plot(arr.real, arr.imag)
# print("--")
# plt.show()


class Complex(object):
    def __init__(self):
        self.arr = np.array([], dtype = complex)
        self.theta = 2*np.pi # 1 full circle, can be adjusted

    def populate_complex_array(self, n : complex) -> np.ndarray :
        angle = np.angle(n)
        print("Initial number : " + str(n))
        print("Initial angle : " + str(round(angle, 2)) + " radian, or " + str(round(np.degrees(angle), 2)) + " degrees" )
        b = np.array([n], dtype = complex)
        self.arr = np.concatenate((self.arr, b))
        return self.arr

    def definition_of_e(self, n): # lim as n -> inf of (1 + i/n)^n = cos(1) + sin(1)*i with modulus = 1
        num = complex(1 + (self.theta/n)*1j)
        print(str(num) + " length: " + str(np.abs(num)) + " degree in radian : " + str(np.angle(num)))
        for i in range(n):
            num *= (1 + (self.theta/n)*1j)
            self.populate_complex_array(num)
            print('-' * 40)
            print(str(num) + " length: " + str(np.abs(num)) + " degree in radian : " + str(np.angle(num)))
        self.argand(self.arr)

    def argand(self, a):
        fig, ax = plt.subplots()
        for x in range(len(a)):
            plt.plot([0,a[x].real],[0,a[x].imag],'ro',label='python')
        limit=np.max(np.ceil(np.absolute(a))) # set limits for axis
        plt.xlim((-limit,limit))
        plt.ylim((-limit,limit))
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_position('zero')
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.show()

c1 = Complex()
c1.definition_of_e(30) 

# x = np.linspace(0.2,10,100)
# fig, ax = plt.subplots()
# ax.plot(x, 1/x)
# ax.plot(x, np.log(x))
# ax.set_aspect('equal')
# ax.grid(True, which='both')

# # set the x-spine (see below for more info on `set_position`)
# ax.spines['left'].set_position('zero')

# # turn off the right spine/ticks
# ax.spines['right'].set_color('none')
# ax.yaxis.tick_left()

# # set the y-spine
# ax.spines['bottom'].set_position('zero')

# # turn off the top spine/ticks
# ax.spines['top'].set_color('none')
# ax.xaxis.tick_bottom()
