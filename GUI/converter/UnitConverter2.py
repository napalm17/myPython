from tkinter import *
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.geometry("520x220")
#root.iconbitmap('Rulers.ico')
root.title("Units Converter")
myfont = font.Font(family="Helvetica")
bg1 ="Khaki"
frame_1 = LabelFrame(root,text="lbs to kg converter",padx=93,pady=10,bg=bg1)
frame_1.grid(row=0,column=0,padx=2,pady=2)


kg_label = Label(frame_1,text="kg",bg=bg1)
lbs_label = Label(frame_1,text="lbs",bg=bg1)

kg_ent = Entry(frame_1,borderwidth=2,width=10,bg="beige")
lbs_ent = Entry(frame_1,borderwidth=2,width=10,bg="beige")
def setzero():
    kg_ent.delete(0,END)
    lbs_ent.delete(0,END)
    kg_ent.insert(0,0)
    lbs_ent.insert(0,0)
setzero()

def converter():
        if float(kg_ent.get()) == 0.0:
            kg_ent.insert(0, round(float(lbs_ent.get())*0.4535,2))
        elif float(lbs_ent.get()) == 0.0:
            lbs_ent.insert(0, round(float(kg_ent.get())*2.205,2))
        else:
            messagebox.showerror("Can't convert","Please clear the inputs!")


convert_lbl = Label(frame_1,text=" ⮂ ",bg=bg1)

convert_button = Button(frame_1,text="convert",padx=20,bg="skyblue",border=1,command=converter)
convert_button['font'] = myfont

clear_button = Button(frame_1,text="clear",padx=30,bg="coral",border=1,command=setzero)
clear_button['font'] = myfont



a = 0
l = [kg_ent, kg_label, convert_lbl, lbs_ent, lbs_label]
for i in l:
    i['font'] = myfont
    i.grid(row=0,column=a)
    a += 1

convert_button.grid(row=1,column=0,columnspan=1)
clear_button.grid(row=1,column=3,columnspan=1)

###########################################################################

bg2 = "#98FB98"
frame_2 = LabelFrame(root,text="cm to inches converter",padx=75,pady=10,bg=bg2)
frame_2.grid(row=1,column=0,padx=2,pady=2)

cm_label = Label(frame_2,text="cm",bg=bg2)
inch_label = Label(frame_2,text="inches",bg=bg2)

cm_ent = Entry(frame_2,borderwidth=2,width=10,bg="#D0F0C0")
inch_ent = Entry(frame_2,borderwidth=2,width=10,bg="#D0F0C0")
def setzero():
    cm_ent.delete(0,END)
    inch_ent.delete(0,END)
    cm_ent.insert(0,0)
    inch_ent.insert(0,0)
setzero()

def converter():
        if float(cm_ent.get()) == 0.0:
            cm_ent.insert(0, round(float(inch_ent.get())*2.54, 2))
        elif float(inch_ent.get()) == 0.0:
            inch_ent.insert(0, round(float(cm_ent.get())*0.3937, 2))
        else:
            messagebox.showerror("Can't convert","Please clear the inputs!")


convert_lbl = Label(frame_2,text=" ⮂ ",bg=bg2)

convert_button = Button(frame_2,text="convert",padx=20,bg="steelblue",border=1,command=converter)
convert_button['font'] = myfont

clear_button = Button(frame_2,text="clear",padx=30,bg="salmon",border=1,command=setzero)
clear_button['font'] = myfont

a = 0
l2 = [cm_ent, cm_label, convert_lbl, inch_ent, inch_label]
for i in l2:
    i['font'] = myfont
    i.grid(row=0,column=a)
    a += 1

convert_button.grid(row=1,column=0)
clear_button.grid(row=1,column=3)

mainloop()
