from matplotlib import pyplot as plt
import numpy as np

plt.style.use('seaborn-deep')
a = 0
b = -20
c = 0
d = 40
x = np.linspace(-100, 100,500)
y = a*x**3 + b*x**2 + c*x + d
y1 = 3*a*x**2 + 2*b*x + c
y2 = 6*a*x + 4*b

ax = plt.gca()

ax.plot(x, y)

ax.plot(x, y1)
ax.plot(x, y2)
ax.grid(True)
ax.yaxis.tick_right()

#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
#ax.spines['top'].set_color('none')

plt.show()

