import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()

x = np.linspace(-np.pi, np.pi, 100)
y = 2*np.sin(x)

ax = plt.gca()

ax.plot(x, y)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.xlim(-np.pi,np.pi)


plt.show()
