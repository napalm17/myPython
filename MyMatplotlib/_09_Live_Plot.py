import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []
ycos = []
index = count()
def animate(i):
    x_vals.append(0.1*i)
    y_vals.append(np.sin(0.1*i))
    ycos.append(np.cos(0.1*i))
    plt.cla()
    plt.plot(x_vals,y_vals)
    plt.plot(x_vals, ycos)
ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']
