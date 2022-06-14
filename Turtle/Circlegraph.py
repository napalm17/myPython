import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
r = 10
a = 20.0
colors = ['#F44336','#E91E63','#9C27B0','#3F51B5','#03A9F4','#4CAF50','#FFC107']
for i in range(50):
    for mycolor in colors:
        turtle.color(mycolor)
        turtle.circle(r)
        turtle.left(a)
        r += 1
        if a > -5:
            a -= -4
        elif a <= 0:
            a += 5
        print(a)

turtle.hideturtle()
turtle.done()