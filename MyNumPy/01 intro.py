import numpy as np

a = np.array([1, 2, 3], dtype = 'int16')
print(a)

b = np.array([[9,8,7,6],[5,4,3,2]])
print(b)
print(a.ndim)
print(b.ndim)
print(a.shape)
print(b.shape)
print(a.dtype)
print(a.itemsize)
print(b.size)
print(b.itemsize)

c = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1,2,3,4,5,6,7,8,9,10]])
print(c[1,2])
print(c[0,:])
print(c[:,3])
print(c[0,1:9:3])
c[:,0] = 77


k = np.array([0,1,2])
l = k.copy()
l[0] = 333
