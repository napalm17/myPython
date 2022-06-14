from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices,shadow=True, startangle=90 ,autopct='%1.1f%%' ,labels=labels, explode=explode,wedgeprops={'edgecolor': 'black'})

plt.title("Popular Programming Languages")
plt.tight_layout()
plt.show()

