import numpy as np

arr = np.array([[1, 0], [2, 3]], int)


u = []
for i in range(4):
    print("------")
    a = np.rot90(arr, i)
    b = np.flip(np.rot90(a, 1), axis=0)
    u.extend([list(a.flatten()), list(b.flatten())])


for i in u:
    temp = i[0]
    i[0] = i[1]
    i[1] = temp

print(u)

u = [[0, 1, 2, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0], [2, 1, 0, 3], [1, 0, 3, 2], [0, 3, 2, 1],  [3, 2, 1, 0]]

for i in u:
    print()
inc = 1
for x in range(len(u)):
    for y in range(len(u)):
        l = []
        for i in u[x]:
            l.append(u[y][i])

        print(f"{inc}) {x + 1} * {y + 1} = {u.index(l) + 1}")
        inc += 1

