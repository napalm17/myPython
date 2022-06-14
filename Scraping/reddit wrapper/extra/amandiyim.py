with open('progs.txt', 'r') as f:
    l = f.read().split('\n')


l2 = []
for i in l:
    l2.append(i[7:])

with open('progs.txt', 'w') as f:
    for i in l2:
        f.write(i + "\n")