from tkinter import *
import tkinter.font as font
from matplotlib import pyplot as plt
import numpy as np

root = Tk()
myfont = font.Font(size="18",family= "Cambria", slant="italic")
root.option_add("*Font","Cambria")
root.option_add("*Size","10")
root.geometry("+800+200")
root.title("Math Graph")

def hidden_one(txt):
    try:
        for x in ["x⁴ +", "x³ +", "x² +", "x +"]:
            txt = txt.replace(" 0" + x, "")
            txt = txt.replace("0.0" + x, "")
        txt = txt.replace("1x", "x")
        txt = txt.replace("1.0x", "x")
        txt = txt.replace("+ 0 ", "")
        txt = txt.replace("+ -", "-")
    except:
        pass
    return txt
def main(a, b, c, d):
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    fintegtext = "  𝐹(x) = {}x⁴ + {}x³ + {}x² + {}x + 𝘊 ".format(round(a/4, 2), round(b/3,2), round(c/2,2), d)
    ftext = "   𝘧(x) = {}x³ + {}x² + {}x + {} ".format(a, b, c, d)
    f1text = " 𝘧 '(x) = {}x² + {}x + {} ".format(3*a, 2*b, c)
    f2text = "𝘧 ''(x) = {}x + {} ".format(2*3*a, 2*b)
    fintegtext = hidden_one(fintegtext)
    ftext = hidden_one(ftext)
    f1text = hidden_one(f1text)
    f2text = hidden_one(f2text)
    finteg_label = Label(frame2, text=fintegtext).grid(column=0,sticky=W)
    f_label = Label(frame2, text=ftext).grid(column=0,sticky=W)
    f1_label = Label(frame2, text=f1text).grid(column=0,sticky=W)
    f2_label = Label(frame2, text=f2text).grid(column=0,sticky=W)

    x = np.linspace(-50, 51, 100000)
    def f0(x):
        return (a/4 * x ** 4) + (b/3 * x ** 3) + (c/2 * x ** 2) + (d * x)
    def f(x):
        return (a * x ** 3) + (b * x ** 2) + (c * x) + d
    def f1(x):
        return (a * 3 * x ** 2) + (b * 2 * x) + c
    def f2(x):
        return (a * 6 * x) + (b * 2)
    def extremes(y, type):
        text = type
        new = 10**10
        for x1, y1 in zip(x, y):
            if -0.1 < y1 < 0.1 and not new-0.5 < x1 < new+0.5:
                new = x1
                val = round(f(x1),1)
                valx = round(x1, 1)
                if type == "Roots: ":
                    val = 0
                if valx == -0.0:
                    valx = 0
                text += "({} | {})  ".format(valx, val)
        if text == type:
            text += "None"
        point = Label(frame3, text=text)
        point.grid(sticky=W)

    extremes(f(x),"Roots: ")
    extremes(f1(x), "Extreme Values: ")
    extremes(f2(x),"Inflection Point: ")

    plt.close('all')
    fig, ax = plt.subplots()
    #ax = plt.gca()
    ax.plot(x, f(x), label="f(x)")

    ax.plot(x, f0(x), label="F(x)")
    ax.plot(x, f1(x), label="f '(x)")
    ax.plot(x, f2(x), label="f ''(x)")
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-75, 100, emit=False)
    ax.legend()
    plt.tight_layout()
    plt.show()

frame1 = LabelFrame(root, text="Enter the terms:", padx=20)
frame1.grid(row=2, sticky= W+E)
frame2 = LabelFrame(root, text="Related Functions:", padx=20, pady=10)
frame2.grid(ipadx=20,row=0, sticky= W+E)
frame3 = LabelFrame(root, text="Important Points:", padx=20, pady=10)
frame3.grid(row=1, sticky= W+E)


fxlabel0 = Label(frame1, text="𝘧(x) = ").grid(row=0,column=0,ipady=20)
x3label = Label(frame1, text="x³ + ").grid(row=0,column=2)
x2label = Label(frame1, text="x² + ").grid(row=0,column=4)
x1label = Label(frame1, text="x + ").grid(row=0,column=6)

a_entry = Entry(frame1,borderwidth=2,width=3,bg="#EAEDED")
b_entry = Entry(frame1,borderwidth=2,width=3,bg="#EAEDED")
c_entry = Entry(frame1,borderwidth=2,width=3,bg="#EAEDED")
d_entry = Entry(frame1,borderwidth=2,width=3,bg="#EAEDED")

entries = [a_entry, b_entry, c_entry, d_entry]
for e, i in zip(entries, range(1,8)):
    e.insert(0,i)
    e.grid(row=0, column=2*i - 1)

button1 = Button(root,text="Show Graph",command=lambda: main(int(a_entry.get()), int(b_entry.get()), int(c_entry.get()), int(d_entry.get())),relief="groove",overrelief="sunken",borderwidth=3
             ,bg="Crimson",fg="#EAEDED",cursor="hand2").grid(row=3,ipadx=150,sticky=W+E)

root.mainloop()