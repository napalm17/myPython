from tkinter import *
import tkinter.font as font
import random as rn
from tkinter import messagebox as msg
from itertools import cycle, islice
root = Tk()

cards = [["2",2],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9],["10",10],["J",10],["Q",10],["K",10],["A",11]]
suits = [["♥","#D40000"],["♦","#D40000"],["♠","Black"],["♣","Black"]]
def appending(range1, range2, liste):
    for i in range(range1):
        for a, b in zip(range(range2),liste):
            liste.append(b)
appending(12, 4, suits)
appending(4, 13, cards)



root.geometry("300x400+550+100")
root.title("Blackjack")
root.iconbitmap('blackjack.ico')
my_font = font.Font(family="Palatino")
e_font = font.Font(family="Palatino",size=10)
title_font = font.Font(family="Palatino",underline="yes")
boldmaker = font.Font(family="Palatino",weight="bold")

title = Label(root,text="★║ Blackjack ║★",borderwidth=1,relief="solid")
title['font'] = boldmaker
title.grid(row=0, column=0,columnspan=2)


myframe = LabelFrame(root,text="    Your Hand    ",padx=25)
myframe['font'] = title_font


dealer_frame = LabelFrame(root,text="  Dealer's Hand  ",padx=25)
dealer_frame['font'] = title_font

myframe.grid(row=1,column=0,padx=2,pady=2,sticky=N)
dealer_frame.grid(row=1,column=1,padx=2,pady=2,sticky=N)
my_score = deal_score = 0
def init():
    global deck
    deck = []
    for x, y in zip(cards, suits):
        deck.append([x, y])
    global my_score
    global deal_score
    global dealcard_1
    hit.configure(state='normal')
    stand.configure(state='normal')
    for widget in myframe.winfo_children():
        widget.destroy()
    for widget in dealer_frame.winfo_children():
        widget.destroy()
    global my_sum
    global deal_sum
    mycard1 = rn.choice(deck)
    deck.remove(mycard1)
    mycard2 = rn.choice(deck)
    deck.remove(mycard2)


    mycard_1 = Label(myframe,text=mycard1[0][0] + mycard1[1][0], fg=mycard1[1][1])
    mycard_1['font'] = boldmaker
    mycard_2 = Label(myframe,text=mycard2[0][0] + mycard2[1][0], fg=mycard2[1][1])
    mycard_2['font'] = boldmaker
    mycard_1.grid(row=0,column=0)
    mycard_2.grid(row=1,column=0)

    line1 = Label(myframe,text="┅┅┅┅")
    line1['font'] = boldmaker
    line1.grid(row=2,column=0)

    dealcard2 = rn.choice(deck)
    deck.remove(dealcard2)

    dealcard_1 = Label(dealer_frame, text="??")
    dealcard_1['font'] = boldmaker
    dealcard_2 = Label(dealer_frame,text=dealcard2[0][0] + dealcard2[1][0], fg=dealcard2[1][1])
    dealcard_2['font'] = boldmaker
    dealcard_1.grid(row=0, column=0)
    dealcard_2.grid(row=1, column=0)

    line2 = Label(dealer_frame, text="┅┅┅┅")
    line2['font'] = boldmaker
    line2.grid(row=2, column=0)

    my_sum = mycard1[0][1] + mycard2[0][1]
    deal_sum = dealcard2[0][1]
    if my_sum >= 21:
        msg.showinfo("Result", "  Blackjack\n" + " YOU WIN!")
        my_score += 1
    if deal_sum == 21:
        msg.showinfo("Result", "  Blackjack\n" + "DEALER WINS!")
        deal_score += 1

def hitfunc():
    global my_score
    global deal_score
    global my_sum
    mycard1 = rn.choice(deck)
    deck.remove(mycard1)
    mynew = Label(myframe,text=mycard1[0][0] + mycard1[1][0], fg=mycard1[1][1])
    mynew['font'] = boldmaker
    mynew.grid(column=0)
    my_sum = my_sum + mycard1[0][1]
    if my_sum == 21:
        show()
        disable()
        msg.showinfo("1Result", "  Blackjack\n" + " YOU WIN!")
        my_score += 1
    if my_sum > 21:
        show()
        disable()
        msg.showinfo("Result","You have: " + str(my_sum) + "\nBUSTED, DEALER WINS!")
        deal_score += 1
    print(my_sum)

def show():
    global deal_sum
    dealcard1 = rn.choice(deck)
    deck.remove(dealcard1)
    dealcard_1.configure(text=dealcard1[0][0] + dealcard1[1][0], fg=dealcard1[1][1])
    deal_sum += dealcard1[0][1]
    return deal_sum
def disable():
    hit.configure(state='disabled')
    stand.configure(state='disabled')
def standfunc():
    show()
    disable()
    global my_score
    global deal_score
    global deal_sum
    info = "You have: " + str(my_sum) + "\nDealer has: " + str(deal_sum)
    if deal_sum > my_sum:
        msg.showinfo("Result",info + "\nDEALER WINS!")
    while deal_sum <= my_sum:
        dealcard1 = rn.choice(deck)
        dealnew = Label(dealer_frame,text=dealcard1[0][0] + dealcard1[1][0], fg=dealcard1[1][1])
        dealnew['font'] = boldmaker
        deal_sum = deal_sum + dealcard1[0][1]
        dealnew.grid(column=0)
        info = "You have: " + str(my_sum) + "\nDealer has: " + str(deal_sum)
        if deal_sum > 21:
            msg.showinfo("Result", info + "\nYOU WIN!")
            my_score += 1
            break
        elif deal_sum > my_sum:
            msg.showinfo("Result", info + "\nDEALER WINS!")
            deal_score += 1
            break


def scoreboard():
    scores = Label(root, text="YOU: " + str(my_score) + " HOUSE: " + str(deal_score), pady=10)
    scores['font'] = my_font
    scores.grid(row=5, column=0, columnspan=2)




hit = Button(root,text="Hit",bg="#D40000",fg="White",padx=55,borderwidth=2,relief="groove",command=hitfunc,state=DISABLED,overrelief="sunken",activeforeground="#D40000")
hit['font'] = my_font
hit.grid(row=2,column=0)
stand = Button(root,text="Stand",bg="#151515",fg="White",padx=45,borderwidth=2,relief="groove",command=standfunc,state=DISABLED,overrelief="sunken",activeforeground="#151515")
stand['font'] = my_font
stand.grid(row=2,column=1)
play = Button(root,text="Play A New Round",bg="#003A09",fg="White",padx=66,command=init,borderwidth=2,relief="groove",overrelief="sunken",activeforeground="#003A09")
play['font'] = my_font
play.grid(row=3,column=0,columnspan=2)
score = Button(root,text=" Show Scoreboard ",bg="#4C4A4A",fg="White",padx=66,command=scoreboard,borderwidth=2,relief="groove",overrelief="sunken")
score['font'] = my_font
score.grid(row=4,column=0,columnspan=2)



mainloop()

