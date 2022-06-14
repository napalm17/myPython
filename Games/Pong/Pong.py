import turtle
import random as rn
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#280B4C")
wn.setup(width=800,height=600)
wn.tracer(0)

pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("#148C86")
pad_1.shapesize(stretch_wid=4, stretch_len=1)
pad_1.penup()
pad_1.goto(-350,0)

pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.color("#8C141A")
pad_2.shapesize(stretch_wid=4, stretch_len=1)
pad_2.penup()
pad_2.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#ECEE31")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = -0

score_1 = score_2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("White")
pen.hideturtle()
pen.goto(0,260)
pen.write("YOU: 0                                                  COMPUTER: 0", align="center",font=("Helvetica",24,"normal"))

for i in range(-300,300,50):
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.penup()
    pen1.color("#3AA71A")
    pen1.hideturtle()
    pen1.goto(0, i)
    pen1.write("I", align="center",
              font=("Helvetica", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.color("White")
pen2.hideturtle()
pen2.goto(0,-200)
pen2.write("Press SPACEBAR to Play", align="center",font=("Helvetica",24,"normal"))
def init():
    pen2.clear()
    ball.dx = 5
    ball.dy = -6

def up1():
    y = pad_1.ycor()
    if y + 55 < 300:
        y += 20
        pad_1.sety(y)
def down1():
    y = pad_1.ycor()
    if y - 55 > -300:
        y -= 20
        pad_1.sety(y)
'''def up2():
    y = pad_2.ycor()
    if y + 55 < 300:
        y += 20
        pad_2.sety(y)
def down2():
    y = pad_2.ycor()
    if y - 55 > -300:
        y -= 20
        pad_2.sety(y)
'''
wn.listen()
wn.onkeypress(init, " ")
wn.onkeypress(up1, "w")
wn.onkeypress(down1, "s")
#wn.onkeypress(up2, "Up")
#wn.onkeypress(down2, "Down")

def game():
    global score_1
    global score_2
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.xcor() > 390:
        ball.goto(0, 280)
        ball.dx = -1 * rn.randrange(3, 6, 2)
        ball.dy = rn.randrange(-1,2,2) * rn.randrange(6, 8)
        score_1 +=1
        pen.clear()
        pen.write("YOU: {}                                                  COMPUTER: {}".format(score_1,score_2), align="center", font=("Helvetica", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 280)
        ball.dx = rn.randrange(3, 6, 2)
        ball.dy = rn.randrange(-1,1,2) * rn.randrange(6, 8)
        score_2 += 1
        pen.clear()
        pen.write("YOU: {}                                                  COMPUTER: {}".format(score_1,score_2), align="center", font=("Helvetica", 24, "normal"))

    elif ball.xcor() == pad_2.xcor()-20 and int(ball.ycor()) in range (int(pad_2.ycor())-60, int(pad_2.ycor())+60):
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.xcor() == pad_1.xcor()+20 and int(ball.ycor()) in range (int(pad_1.ycor())-80, int(pad_1.ycor())+80):
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #AI
    if ball.dx > 0:
        r = rn.randrange(2, 9, 2)
        y = pad_2.ycor()
        if pad_2.ycor() < ball.ycor():
            if y + 55 < 300:
                y += r
                pad_2.sety(y)
        elif pad_2.ycor() > ball.ycor():
            if y - 55 > -300:
                y -= r
                pad_2.sety(y)
    wn.ontimer(game,10)


game()

turtle.mainloop()
