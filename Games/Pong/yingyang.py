import turtle as tr
import winsound
import random as rn

wn = tr.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

ying = tr.Turtle()
yang = tr.Turtle()
def f(x, a, b, color1, color2):
    x.speed(0)
    x.shape("circle")
    x.color(color1, color2)
    x.shapesize(stretch_wid=3, stretch_len=3)
    x.penup()
    x.goto(a, b)


f(ying, -100, 0, "white", "black")
f(yang, 100, 0, "white", "white")
ying.left(90)
yang.right(90)
a = 1
while True:

    ying.forward(a)
    ying.right(0.5)
    yang.forward(a)
    yang.right(0.5)

    wn.update()

tr.mainloop()