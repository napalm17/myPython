from tkinter import *
import tkinter.font as font
import politic_compass as pc
import random as rn

with open('questions.txt', 'r') as f:
    l = f.read().split('\n')
econ = [x.replace(" -eko-", "") for x in l if "eko" in x]
cult = [y.replace(" -kult-", "") for y in l if "kult" in y]
state = [z.replace(" -devlet-", "") for z in l if "devlet" in z]

class Quest:
    vars = []
    def __init__(self, questions):
        self.questions = questions
    def gui(self):
        for widget in mainframe.winfo_children():
            widget.destroy()
        row = 0
        for i in self.questions:
            Quest.vars.append(IntVar())
            quest_frame = LabelFrame(mainframe)
            quest_frame.grid(sticky=W+E, column=0, row=row)
            ans_frame = LabelFrame(mainframe)
            ans_frame.grid(column=1, row=row, sticky=W+E)
            Label(quest_frame, text=i).grid(sticky=W, pady=10, column=0, row=row)
            scale = Scale(ans_frame,from_=-3, to=3, var=Quest.vars[row], orient=HORIZONTAL, length=250, activebackground="red")
            num = rn.randint(-3, 3)
            scale.set(0)
            scale.grid(sticky=E, column=1, row=row)
            row += 1
        empty = Label(root, text="")
        empty.grid(row=0, column=1, pady=280)
        empty1 = Label(mainframe, text="", padx=400)
        empty1['font'] = small
        empty1.grid(column=0, row=50)
    def get_total(self):
        total = 0
        for x in Quest.vars:
            total += x.get()
        return total

def control(quests, titles):
    global mainframe, i, Page
    try:
        points.append(Page.get_total())
        mainframe.destroy()
    except:
        pass
    if i < 7:
        mainframe = LabelFrame(root, text=titles[i-1])
        mainframe.grid(column=0,row=0, sticky=W + E + N)
        Page = Quest(quests[i-1])
        Page.gui()
        if i < 2:
            frame0.destroy()
            but.configure(text="Next Page", bg="#f4d03f")
        elif i > 5:
            but.configure(text="Finish Test", bg="#58d68d")
        i += 1
    else:
        but.configure(state=DISABLED)
        coors = [points[x] + points[x+1] for x in range(0, len(points), 2)]
        print(coors)
        root.destroy()
        pc.plot_compass(coors)

root = Tk()
root.geometry("+200+5")
general_font = ('Cambria', 11)
root.option_add("*Font", general_font)
myfont = font.Font(size="14",family= "Cambria")
small = font.Font(size="5",family= "Cambria")
frame0 = LabelFrame(root, text="Welcome!")
frame0.grid(sticky=W+E, row=0, ipady=200, columnspan=2)
frame1 = LabelFrame(root, text="")
frame1.grid(ipadx=400,row=1,columnspan=2)
intro = Label(frame0, text="Your Favorite Political Test Is Now In 3D")
intro['font'] = myfont
intro.pack(expand=1)

quests = [econ[:10], econ[10:], state[:10], state[10:], cult[:10], cult[10:]]
titles = ["Economic:", "Economic:", "Governmental:", "Governmental:","Cultural","Cultural"]
points = []
i = 1

but = Button(frame1,text="Start Test",padx=100, pady=10,bg="#3498db",border=1,relief="groove", command=lambda: control(quests, titles), overrelief="sunken",borderwidth=3,cursor="hand2")
but['font'] = myfont
but.pack(expand=1)
mainloop()


