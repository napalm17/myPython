import numpy as np

a = np.ones((4,3))
print(a)
b = np.full((3,4),2)
print(b)

print(np.matmul(b,a))