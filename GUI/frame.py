from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()


def save():
    pass

frame1 = LabelFrame(root,text="HUMBLE",padx=100,pady=100,bg="Black")
frame1.pack(padx=10,pady=10)
'''frame2 = LabelFrame(frame1,text="DNA",padx=9,pady=9,bg="White")
frame2.pack(padx=80,pady=80)
frame3 = LabelFrame(frame2,text="PRIDE",padx=8,pady=8,bg="Black")
frame3.pack(padx=70,pady=70)
frame4 = LabelFrame(frame3,text="BLOOD",padx=7,pady=7,bg="White")
frame4.pack(padx=60,pady=60)
frame5 = LabelFrame(frame4,text="HUMBLE",padx=10,pady=10,bg="Black")
frame5.pack(padx=30,pady=30)'''

calc_button = Button(frame1,text="E",fg="white",bg="deep sky blue", command=save)
calc_button.grid(row=0,column=0,)

mainloop()