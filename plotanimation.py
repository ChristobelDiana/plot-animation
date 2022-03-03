import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter

fig,axes = plt.subplots(figsize=(12,5))
axes.set_xlim(0,300)
axes.set_ylim(-350,600)
axes.set_title('Multiple Lines Animation')
plt.style.use('seaborn-white')
plt.xlabel("X axis")
plt.ylabel("y axis")
x,y1,y2,y3,y4=[],[],[],[],[]
x_data=range(0,300,3)

l1 = [random.randint(-10,0)+(i**1.7)/13 for i in range(0,200,2)]
l2 = [random.randint(0, 10) + (i ** 1.5) / 11 for i in range(0, 200, 2)]
l3 = [random.randint(-10, 0) - (i ** 1.3) / 7 for i in range(0, 200, 2)]
l4 = [random.randint(-10,0) - (i ** 1.5)/ 9 for i in range(0,200,2)]

def animate(i):
    x.append(x_data[i])
    y1.append(l1[i])
    y2.append(l2[i])
    y3.append(l3[i])
    y4.append(l4[i])
    axes.plot(x,y1,color="red")
    axes.plot(x, y2, color="green")
    axes.plot(x, y3, color="orange")
    axes.plot(x, y4, color="blue")

ani = FuncAnimation(fig,animate,interval=100,frames=100,repeat=False)
plt.show()
#ani.save("multiplelines.gif",writer=PillowWriter(fps=60))
