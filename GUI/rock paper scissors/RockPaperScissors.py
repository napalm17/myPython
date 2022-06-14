from tkinter import *
import tkinter.font as font
import random as rn
from PIL import ImageTk, Image
from tkinter import messagebox as msg

root = Tk()
root.title("Rock Paper Scissors")
#root.iconbitmap('rockpng.ico')

my_font = font.Font(family="Helvetica",weight="bold")




myframe = LabelFrame(root,text="You",padx=20)
myframe['font'] = my_font
myframe.grid(row=0,column=0)

vsimage = ImageTk.PhotoImage(Image.open("battle.png"))
vsimage2 = ImageTk.PhotoImage(Image.open("battle2.png"))

vslabel = Label(root,image=vsimage)
vslabel.grid(row=0,column=1)

compframe = LabelFrame(root,text="     Computer ",padx=17,pady=4)
compframe['font'] = my_font
compframe.grid(row=0,column=2,sticky=N)

myscore = c_score = 0
result_lbl = Label(root, text="")
result_lbl['font'] = my_font
result_lbl.grid(row=1, column=0, columnspan=3)
def play(myvalue):
    global myscore
    global c_score
    vslabel.configure(image=vsimage2)
    mylist = ["Paper","Scissors","Rock"]
    buttons = [mypaper, myscis ,myrock]
    complist = [["Rock", c_rock], ["Paper", c_paper], ["Scissors", c_scis]]
    win = [["Rock", "Scissors"], ["Paper", "Rock"], ["Scissors", "Paper"]]
    compvalue = rn.choice(complist)
    for x,mybutton in zip(mylist,buttons):
        if myvalue == x:
            values = [myvalue, compvalue[0]]
            if myvalue == compvalue[0]:
                result_lbl.configure(text="IT'S A DRAW!")
                mybutton.configure(bg="#F39C12")
                compvalue[1].configure(bg="#F39C12")
            else:
                youwin = False
                for i in win:
                    if values == i:
                        youwin = True
                        result_lbl.configure(text="YOU WIN!")
                        mybutton.configure(bg="#28B463")
                        compvalue[1].configure(bg="#E74C3C")
                        myscore+=1
                        break
                if not youwin:
                    result_lbl.configure(text="COMPUTER WINS!")
                    mybutton.configure(bg="#E74C3C")
                    compvalue[1].configure(bg="#28B463")
                    c_score += 1
    result_lbl.grid(row=1, column=0, columnspan=3)


def reset():
    result_lbl.configure(text="")
    vslabel.configure(image=vsimage)
    buttons = [c_rock, c_paper, c_scis, myrock, mypaper, myscis]
    for but in buttons:
        but.configure(bg="#F0F0F0")

def score():
    score_lbl = Label(root,text="YOU: {}      COMPUTER: {}".format(myscore,c_score))
    score_lbl['font'] = my_font
    score_lbl.grid(row=4,column=0,columnspan=3)
rock1 = ImageTk.PhotoImage(Image.open("rockhand.png"))
paper1 = ImageTk.PhotoImage(Image.open("handpaper.png"))
scis1 = ImageTk.PhotoImage(Image.open("hand-scissors.png"))

rock2 = ImageTk.PhotoImage(Image.open("rockhand2.png"))
paper2 = ImageTk.PhotoImage(Image.open("handpaper2.png"))
scis2 = ImageTk.PhotoImage(Image.open("hand-scissors2.png"))
abg ="#B4C0BE"
myrock = Button(myframe, image=rock2, command=lambda:play("Rock"),borderwidth=4,relief="groove",overrelief="sunken",activebackground=abg)
mypaper = Button(myframe, image=paper2, command=lambda:play("Paper"),borderwidth=4,relief="groove",overrelief="sunken",activebackground=abg)
myscis = Button(myframe, image=scis2, command=lambda:play("Scissors"),borderwidth=4,relief="groove",overrelief="sunken",activebackground=abg)

myrock.grid(row=0, column=0)
mypaper.grid(row=1, column=0)
myscis.grid(row=2, column=0)

c_rock = Label(compframe, image=rock1,borderwidth=4,relief="groove")
c_paper = Label(compframe, image=paper1,borderwidth=4,relief="groove")
c_scis = Label(compframe, image=scis1,borderwidth=4,relief="groove")

c_rock.grid(row=0, column=0)
c_paper.grid(row=1, column=0)
c_scis.grid(row=2, column=0)

resetbut = Button(root,text="Play Again",padx=120,command=reset,bg="#A9CCE3",relief="groove",overrelief="sunken")
resetbut['font'] = my_font
resetbut.grid(row=2,column=0,columnspan=3)
resetbut = Button(root,text="Refresh Scoreboard",padx=75,command=score,bg="#F0B27A",relief="groove",overrelief="sunken")
resetbut['font'] = my_font
resetbut.grid(row=3,column=0,columnspan=3)

score_lbl = Label(root,text="YOU: {}      COMPUTER: {}".format(myscore,c_score))
score_lbl['font'] = my_font
score_lbl.grid(row=4,column=0,columnspan=3)
mainloop()
