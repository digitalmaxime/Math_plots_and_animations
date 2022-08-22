# 
# sentdex chanel
# 
#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

# data = open('asset/stock.txt','r')
# for line in data:
#     print(line.split("\n")[0])
# print("*"*40)
# *************
# data.seek(0)
# line = data.readline()
# while line != "":
#     print(line.split("\n")[0])
#     line = data.readline()

def animate(i):
    data = open('asset/stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    
    for line in lines:
        if (line == ""):
            continue
        x, y = line.split(',') # Delimiter is comma    
        xs.append(float(x))
        ys.append(float(y))
   
    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')	
	
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()
