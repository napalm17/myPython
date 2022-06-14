def planets():
    all = [["Sun","1,989E30 kg"],["Mercury","3,285E23 kg"],["Venus","4,867E24 kg"],["Earth","5,972E24 kg"],["Mars","6,39E23 kg"],
           ["Saturn","5,683E26 kg"],["Jupiter","1,898E27 kg"],["Uranus","8,681E25 kg"],["Neptune","1,024E26 kg"]]
    planet_name = input("Enter the name of the planet, whose total mass you'd like to learn?: ")
    for x in range(9):
        if planet_name == all[x][0]:
            print("The total mass of " + all[x][0] + " is " + all[x][1] + ".")
            break
planets()
