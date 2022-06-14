from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font


root = Tk()
root.geometry('300x200')
my_font = font.Font(family="Palatino",size=40)
otherfont = font.Font(family="Comic sans Ms",size=30)

def verdict():
    if var.get() == 1:
        hell = Toplevel()
        hell.geometry('1280x720')
        hell.configure(bg="Black")
        hell.title("HELL")
        hell_label = Label(hell,text="\n\n\n\n\nWelcome to Hell, please suffer in silence.".upper(),bg="Black",fg="Red")
        hell_label['font'] = my_font
        hell_label.pack()
    else:
        hell = Toplevel()
        hell.geometry('1280x720')
        hell.configure(bg="White")
        hell.title("HEAVEN")
        hell_label = Label(hell, text="\n\n\n\n\nWelcome to HEAVEN, please exhibit your Gratitude.".upper(), bg="WHITE",
                           fg="GOLD")
        hell_label['font'] = otherfont
        hell_label.pack()
var = IntVar()

empty = Label(root,text="\n\n\n").pack()
cbox = Checkbutton(root,text="I agree to go to hell.",variable=var)
cbox.deselect()
cbox.pack()
click = StringVar
menu = OptionMenu(root, click,"Heaven","Hell")


button = Button(root,text="OK",command=verdict).pack()

mainloop()