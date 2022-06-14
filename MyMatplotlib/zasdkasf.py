import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in the top left and bottom right corners, and a link between them
cube1 = (x < 10) & (y < 10) & (z < 10)
#cube2 = (x >= 5) & (y >= 5) & (z >= 5)
#link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

# combine the objects into a single boolean array
voxels = cube1

# set the colors of each object
#colors = np.empty(voxels.shape, dtype=object)
#colors[link] = 'red'
#colors[cube1] = 'blue'
#colors[cube2] = 'green'

# and plot everything
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(voxels, facecolors="red")

plt.show()