def sumnums():
    num = input("Number:")
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i])

    print(sum)

sumnums()