check = None
for i in range(0,100):
    for e in range(1,i,1):
        check = True
        if i % e == 0 and e != 1:
            check = False
            break
    if check:
        print(i)