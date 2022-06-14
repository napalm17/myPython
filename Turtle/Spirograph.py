from turtle import *

speed(0)
bgcolor('black')
colors = ['#F44336','#9C27B0','#3F51B5','#03A9F4','#4CAF50','#FFC107']

for i in range(360):
    pencolor(colors[i%6])
    width(i / 250 + 1)
    forward(i)
    left(59)

hideturtle()