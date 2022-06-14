from tkinter import *
from PIL import ImageTk, Image
root = Tk()
photos = ["maad-city-cover.jpg","tpab.jpeg"]
i = 0

def open(i):
    global my_img2
    top = Toplevel()
    my_img2 = ImageTk.PhotoImage(Image.open(photos[i]))
    win_label = Label(top, text="good kid").pack()
    i += 1
    if i < len(photos):
        good_but = Button(top, image=my_img2, command=lambda: open(i)).pack()
    elif i >= len(photos):
        good_but = Button(top, image=my_img2,state=DISABLED).pack()

my_img1 = ImageTk.PhotoImage(Image.open("maad-city-cover.jpg"))
root_label = Label(root ,text="maad city").pack()
maad_but = Button(root,image=my_img1,command=lambda:open(i)).pack()
root.mainloop()