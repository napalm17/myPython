from matplotlib import pyplot as plt

for i in plt.style.available:
    print(i)
plt.style.use('seaborn-deep')
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, label="Python Devs")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, label="Javascript Devs")

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, label="All Devs", color='#17202A', linestyle='--')

plt.xlabel("Age")
plt.ylabel("Median Salary")
plt.title("Median Salary (USD) by Age")

plt.legend()

plt.tight_layout()

#plt.show()

f = plt.figure()
ax = f.add_subplot(243)
ax.yaxis.tick_right()
plt.plot([2,3,4,5])
plt.show()