import turtle as tr
import winsound
import random as rn

wn = tr.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

a = 0.1
r = 100
circle1 = tr.Turtle()
circle1.speed(0)
circle1.shape("circle")
circle1.color("white")
circle1.shapesize(stretch_wid=a*100, stretch_len=a*100)
circle1.penup()
circle1.goto(0, 0)

circle2 = tr.Turtle()
circle2.speed(0)
circle2.shape("circle")
circle2.color("white")
circle2.shapesize(stretch_wid=a*25, stretch_len=a*25)
circle2.penup()
circle2.goto(0, 200)

circle3 = tr.Turtle()
circle3.speed(0)
circle3.shape("circle")
circle3.color("white", "red")

circle3.shapesize(stretch_wid=a*5, stretch_len=a*5)
circle3.penup()
circle3.goto(0, 250)

while True:
    circle2.forward(1)
    circle2.right(0.3)


    circle3.goto(circle2.pos())
    circle3.forward(50)
    circle3.left(0.5)

    circle1.goto(circle2.pos())
    circle1.forward(250)
    circle1.right(0.5)

    wn.update()

tr.mainloop()