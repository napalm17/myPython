import numpy as np

stats = np.array([[9,8,7,6],
                  [5,4,3,2]])

print(np.min(stats, axis=0))
print(np.max(stats, axis=1))
print(np.min(stats[1, :]))
print(np.sum(stats, axis=1))