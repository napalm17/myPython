from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font


root = Tk()
root.title('Images')
root.iconbitmap(r'Photos.ico')
root.configure(bg='Black')
my_font = font.Font(size=16, family='Helvetica bold')

title_label = Label(root,text="Pink Floyd Album Covers",bg='Black', fg='White')
title_label['font'] = my_font
title_label.grid(row=0,column=1)

#root.geometry('500x500')
Animals = ImageTk.PhotoImage(Image.open('animals.jpg'),size='50x50')
Meddle = ImageTk.PhotoImage(Image.open('Meddle.jpeg'),size='50x50')
Wish_You_Were_Here = ImageTk.PhotoImage(Image.open('wishyouwerehere.jpg'),size='50x50')
Dark_Side_of_the_Moon = ImageTk.PhotoImage(Image.open('Dark.jpg'),size='50x50')
images = [Animals,Meddle,Wish_You_Were_Here,Dark_Side_of_the_Moon]
title =["Animals","Meddle","Wish You Were Here","Dark Side of the Moon"]

my_label = Label(image=Animals)
my_label.grid(row=1, column=0, columnspan=3)

my_title = Label(root,text=title[0],bg='Black', fg='White')
my_title['font'] = my_font
my_title.grid(row=2,column=1)

def forward(i):
    global my_label
    global button_for
    global button_back
    global my_title
    my_label.grid_forget()
    my_label = Label(image=images[i-1])
    my_label.grid(row=1, column=0, columnspan=3)
    my_title.grid_forget()
    my_title = Label(root, text=title[i - 1], bg='Black', fg='White')
    my_title.grid(row=2, column=1)
    button_for = Button(root, text=">", padx=100, bg='black', fg='White', command=lambda: forward(i+1))
    button_back = Button(root, text="<", padx=100, bg='black', fg="White", command=lambda: back(i-1))
    if i == 4:
        button_for = Button(root, text=">", padx=100, bg='black', fg='White', state=DISABLED)
    button_back.grid(row=2, column=0)
    button_for.grid(row=2, column=2)
    my_label.grid(row=1, column=0, columnspan=3)


def back(i):
    global my_label
    global button_for
    global button_back
    global my_title
    my_label.grid_forget()
    my_label = Label(image=images[i - 1])
    my_label.grid(row=1, column=0, columnspan=3)
    button_for = Button(root, text=">", padx=100, bg='black', fg='White', command=lambda: forward(i + 1))
    button_back = Button(root, text="<", padx=100, bg='black', fg="White", command=lambda: back(i - 1))
    button_back.grid(row=2, column=0)
    button_for.grid(row=2, column=2)
    my_label.grid(row=1, column=0, columnspan=3)

button_back = Button(root,text="<",padx=100,bg='black',fg="White",command=back)
button_for = Button(root,text=">",padx=100,bg='black',fg='White',command=lambda:forward(2))
button_for['font'] = my_font
button_back['font'] = my_font
button_back.grid(row=2,column=0)
button_for.grid(row=2,column=2)

def menuimg():
    my_label.grid_forget()
    menu_label = Label(image=click.get())
    menu_label.grid(row=1,column=0)


click = StringVar()
click.set("Albums")
menu = OptionMenu(root,click,*images)
menu.grid(row=0,column=0)

menuButton = Button(root,text="Select Image", command=menuimg)
menuButton.grid(row=0,column=1)

root.mainloop()