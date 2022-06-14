from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.iconbitmap(r'IEL.ico')
root.title("Abirechner")
root.geometry("320x297")
my_font = font.Font(family="Palatino")
e_font = font.Font(family="Palatino",size=10)
title_font = font.Font(family="Palatino",weight="bold",underline="yes")
boldmaker = font.Font(family="Palatino",weight="bold")



label_title = Label(root,text="Endnoten",padx=50)
label_title['font'] = title_font
label_title.grid(row=0,column=0,columnspan=2)

label_deu = Label(root,text="Deutsch:")
label_eng = Label(root,text="Englisch:")
label_mat = Label(root,text="Mathe:")
label_phy = Label(root,text="Physik:")
label_bio = Label(root,text="Biologie:")
label_che = Label(root,text="Chemie:")
label_deu['font'] = my_font
label_eng['font'] = my_font
label_mat['font'] = my_font
label_phy['font'] = my_font
label_bio['font'] = my_font
label_che['font'] = my_font
label_deu.grid(row=1,column=0)
label_eng.grid(row=2,column=0)
label_mat.grid(row=3,column=0)
label_phy.grid(row=4,column=0)
label_bio.grid(row=5,column=0)
label_che.grid(row=6,column=0)

e_deu = Entry(root,width=5,borderwidth=2)
e_eng = Entry(root,width=5,borderwidth=2)
e_mat = Entry(root,width=5,borderwidth=2)
e_phy = Entry(root,width=5,borderwidth=2)
e_bio = Entry(root,width=5,borderwidth=2)
e_che = Entry(root,width=5,borderwidth=2)
e_deu['font'] = e_font
e_eng['font'] = e_font
e_mat['font'] = e_font
e_phy['font'] = e_font
e_bio['font'] = e_font
e_che['font'] = e_font
e_deu.grid(row=1,column=1)
e_eng.grid(row=2,column=1)
e_mat.grid(row=3,column=1)
e_phy.grid(row=4,column=1)
e_bio.grid(row=5,column=1)
e_che.grid(row=6,column=1)

def calc(deu,eng,mat,phy,bio,che):
    try:
        global result
        my_score = 2 * (int(deu) + int(eng) + int(mat) + int(phy)) + int(bio) + int(che)
        if my_score > 150:
            error()
        elif my_score > 140:
            result = Label(root,text="1.0")
            result['font'] = boldmaker
            result.grid(row=7,column=1)
        elif my_score < 50:
            result = Label(root, text="Nicht bestanden!")
            result['font'] = boldmaker
            result.grid(row=7, column=1)
        else:
            for score, result in zip(range(50,151,3),range(40,9,-1)):
                if my_score <= score:
                    result = Label(root, text="⇒ "+str(result/10))
                    result['font'] = boldmaker
                    result.grid(row=7, column=1,columnspan=3)
                    break
    except:
        messagebox.showerror(ValueError, "Bitte gib gültige Werte ein!")

def error():
    global result
    result = Label(root, text="Bitte gib\ngültige Werte ein!")
    result['font'] = boldmaker
    result.grid(row=7, column=1)

def clear():
    e_deu.delete(0,END)
    e_eng.delete(0,END)
    e_mat.delete(0,END)
    e_phy.delete(0,END)
    e_bio.delete(0,END)
    e_che.delete(0,END)
    result.grid_forget()

button = Button(root,text="Durchschnittsnote\n Berechnen",bg="gold", command=lambda: calc(e_deu.get(),e_eng.get(),e_mat.get(),e_phy.get(),e_bio.get(),e_che.get()))
button['font'] = my_font
button.grid(row=7,column=0)

clear = Button(root,text=" Löschen ",bg="Black",fg="White",padx=34,command=clear)
clear['font'] = my_font
clear.grid(row=8,column=0)

iel = ImageTk.PhotoImage(Image.open('IEL_Logo.png'))
img_label = Label(root,image=iel)
img_label.grid(row=0,column=4,rowspan=7,columnspan=5)

root.mainloop()