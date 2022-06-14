import numpy as np

print(np.zeros((4,4)))

print(np.full((2,2),99))
b = np.array([[9,8,7,6],[5,4,3,2]])
print(np.full_like(b, 7))

print(np.random.rand(5,6))
print(np.random.randint(-98,93, size=(3,3)))
print(np.identity(6))

a = np.ones((5,5))
a[1:-1,1:-1] = 0
a[2,2] = 9
print(a)

e = np.ones((12,12,12))
print(e)
