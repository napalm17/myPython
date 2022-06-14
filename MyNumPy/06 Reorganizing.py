import numpy as np
before = np.array([[9,8,7,6],
                  [5,4,3,2],
                  [9,8,7,6]])
print(before)

after = before.reshape((2,3,1,2))

print(after)

v1 = np.array([9,8,7,6])
v2 = np.array([5,4,3,2])

total = np.vstack([v1,v2,v2,v1,v2])


print(total)

h1 = np.array([9,8,7,6])
h2 = np.array([5,4,3,2])

totalh = np.vstack([h1,h2])

print(totalh)