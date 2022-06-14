from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Planet masses")
root.configure(bg="black")
root.geometry('250x350')
boldmaker = font.Font(family="Helvetica",weight="bold")
myfont = font.Font(family="Helvetica",size=10)

title = Label(root,text="Select a planet/star:",bg="Black",fg= "White")
title.pack()

masses = [["Sun","1,989E30 kg","yellow"],["Mercury","3,285E23 kg","maroon",],["Venus","4,867E24 kg","orange"],
          ["Earth","5,972E24 kg","steelblue"],["Mars","6,39E23 kg","crimson"],
           ["Saturn","5,683E26 kg","gold"],["Jupiter","1,898E27 kg","sienna"],
          ["Uranus","8,681E25 kg","cyan"],["Neptune","1,024E26 kg","navy"]]
#colors = ["yellow","beige","orange","steelblue","crimson","gold","copper","cyan","navy"]

m = StringVar()
m.set("Sun")
for planet, mass, color in masses:
    Radiobutton(root,text=planet,var=m,value=mass,bg="black",fg=color).pack()
def massfinder(value):
    global mylabel
    mylabel = Label(root,text=value,bg="black",fg="White")
    mylabel['font'] = myfont
    mylabel.pack()
    messagebox.showinfo("mass",value)
def clear():
    mylabel.pack_forget()

button = Button(root,text="Show its mass",bg="gray",fg="white",command=lambda: massfinder(m.get()))
button['font'] = myfont
button.pack()
clearbut = Button(root,text="Clear",bg="Maroon",fg="white",command=clear)
clearbut['font'] = myfont
clearbut.pack()
root.mainloop()
