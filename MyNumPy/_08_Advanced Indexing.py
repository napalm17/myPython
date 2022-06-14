from MyNumPy import _07_load_data as data
import numpy as np
a = data.filedata
b = a[a > 100]

print(b)

d = []

for i in range(12):
    d.append(i)

e = np.array(d)
print(e[4:7])

print(np.any(a > 90, axis=0))