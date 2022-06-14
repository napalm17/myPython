from tkinter import *
import tkinter.font as font
import winsound
from pydub import AudioSegment
from pydub.playback import play
import simpleaudio
notes = ["C","C♯","D","E♭","E","F","F♯","G","G♯","A","B♭","B","C","C♯","D","E♭","E","F","F♯","G","G♯","A", "B♭", "B"]
root = Tk()
root.configure(bg="black")
root.title("Chordfinder")
root.geometry("485x300")
my_font = font.Font(family="Palatino")
title_font = font.Font(family="Palatino",weight="bold")
boldmaker = font.Font(family="Palatino",weight="bold")

def note(root):
    sound1 = AudioSegment.from_file("As3.wav")
    sound2 = AudioSegment.from_file("As3.wav")
    sound3 = AudioSegment.from_file("As3.wav")

    com1 = sound1.overlay(sound2)
    combined = sound3.overlay(com1)

    combined.export("combined.wav", format='wav')
    play(combined)
    global i

    if root not in notes:
        print("Please enter a valid note!")
    for i in range(24):
        if root == notes[i]:
            return i
def majmin(type):
    global chord
    global scale

    if type == "major":
        chord = Label(root, text="The notes of the " + notes[i] + " major chord are " + notes[i] + ", " + notes[i + 4]
                                 + " and " + notes[i + 7] + ".",bg="Black",fg="deepskyblue")
        chord['font'] = my_font

        scale = Label(root, text="The notes of the " + notes[i] + " major scale are "
                        + notes[i] + " " + notes[i + 2] + " " + notes[i + 4] + " " + notes[i + 5] + " "
                        + notes[i + 7] + " " + notes[i + 9] + " " + notes[i + 11] + " " + notes[i + 12] + ".",bg="Black",fg="deepskyblue")
        scale['font'] = my_font
    elif type == "minor":
        chord = Label(root, text="The notes of the " + notes[i] + " minor chord are " + notes[i] + "," + notes[i + 3] + " and " +
              notes[i + 7] + ".",bg="Black",fg="teal")
        chord['font'] = my_font
        scale = Label(root, text="The notes of " + notes[i] + " minor scale are: "
              + notes[i] + " " + notes[i + 2] + " " + notes[i + 3] + " " + notes[i + 5] + " "
              + notes[i + 7] + " " + notes[i + 8] + " " + notes[i + 10] + " " + notes[i + 12] + ".",bg="Black",fg="teal")
        scale['font'] = my_font
    return chord,scale

def show():
    chord.grid(row=4, column=0, columnspan=12)
    scale.grid(row=5, column=0, columnspan=12)
def clear():
    chord.grid_forget()
    scale.grid_forget()
fg0 = "deepskyblue"
my_title = Label(root,text="Music Theory Calculator\n".upper(),fg=fg0,bg="Black")
my_title['font'] = title_font
my_title.grid(row=0,column=0,columnspan=12,rowspan=2)
fg = "White"
bg1 = "lightseagreen"
bg2 = "teal"
c_button = Button(root,text=" C ",command=lambda:note("C"),fg=fg,bg=bg1)
cs_button = Button(root,text="C♯",command=lambda:note("C♯"),fg=fg,bg=bg2)
d_button = Button(root,text=" D ",command=lambda:note("D"),fg=fg,bg=bg1)
eb_button = Button(root,text="E♭",command=lambda:note("E♭"),fg=fg,bg=bg2)
e_button = Button(root,text=" E ",command=lambda:note("E"),fg=fg,bg=bg1)
f_button = Button(root,text=" F ",command=lambda:note("F"),fg=fg,bg=bg2)
fs_button = Button(root,text="F♯",command=lambda:note("F♯"),fg=fg,bg=bg1)
g_button = Button(root,text=" G ",command=lambda:note("G"),fg=fg,bg=bg2)
gs_button = Button(root,text="G♯",command=lambda:note("G♯"),fg=fg,bg=bg1)
a_button = Button(root,text=" A ",command=lambda:note("A"),fg=fg,bg=bg2)
bb_button = Button(root,text="B♭",command=lambda:note("B♭"),fg=fg,bg=bg1)
b_button = Button(root,text=" B ",command=lambda:note("B"),fg=fg,bg=bg2)

c_button['font'] = my_font
cs_button['font'] = my_font
d_button['font'] = my_font
eb_button['font'] = my_font
e_button['font'] = my_font
f_button['font'] = my_font
fs_button['font'] = my_font
g_button['font'] = my_font
gs_button['font'] = my_font
a_button['font'] = my_font
bb_button['font'] = my_font
b_button['font'] = my_font

c_button.grid(row=2,column=0)
cs_button.grid(row=2,column=1)
d_button.grid(row=2,column=2)
eb_button.grid(row=2,column=3)
e_button.grid(row=2,column=4)
f_button.grid(row=2,column=5)
fs_button.grid(row=2,column=6)
g_button.grid(row=2,column=7)
gs_button.grid(row=2,column=8)
a_button.grid(row=2,column=9)
bb_button.grid(row=2,column=10)
b_button.grid(row=2,column=11)

major_button = Button(root,text="Major",fg=fg,bg="dark turquoise",command=lambda: majmin("major"),padx=89)
minor_button = Button(root,text="Minor",fg=fg,bg="teal",command=lambda: majmin("minor"),padx=89)
major_button['font'] = title_font
minor_button['font'] = title_font
major_button.grid(row=3,column=0,columnspan=6)
minor_button.grid(row=3,column=6,columnspan=6)

calc_button = Button(root,text="Calculate",fg="white",bg="deep sky blue",command=show,pady=10)
calc_button['font'] = my_font
calc_button.grid(row=6,column=0,columnspan=12,sticky=N+S)

clear_button = Button(root,text="Clear",fg=fg,bg="darkslategray",command=clear,padx=17,anchor=E)
clear_button['font'] = my_font
clear_button.grid(row=7,column=0,columnspan=3)
root.mainloop()