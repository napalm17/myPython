while True:
    print("\nEnter the numbers, whose mean average you'd like to learn: ")
    i = sum = 0
    for i in range(100):
        ans = input(str(i+1) + ". Number: ")
        if ans == "ok":
            break
        else:
            sum += int(ans)
    print("Mean average is " + str(round(sum / i, 2)))
