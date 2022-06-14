from tkinter import *
import tkinter.font as font
from pydub import AudioSegment
from pydub.playback import play
from functools import partial
from PIL import ImageTk,Image

root = Tk()
myfont = font.Font(size="18",family= "helveticaneue",weight="bold")
general_font = ('Helveticaneue', 14)
root.option_add("*Font", general_font)
root.geometry("+400+20")
root.title("Keyfinder")
#root.iconbitmap('icon.ico')

class Key:
    def __init__(self,mynote,mytype):
        self.mynote = mynote
        self.mytype = mytype
        for i in range(12):
            if notes[i] == self.mynote:
                self.i = i
                break
        i = self.i
        if self.mytype == "Major":
            self.scale = [notes[i], notes[i + 2], notes[i + 4], notes[i + 5], notes[i + 7], notes[i + 9], notes[i + 11]]
            self.soundscale = [sounds[i], sounds[i + 2], sounds[i + 4], sounds[i + 5], sounds[i + 7], sounds[i + 9],
                               sounds[i + 11]]
            self.symbols = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
            self.code1 = "m"
            self.code2 = ""
        elif self.mytype == "Minor":
            self.scale = [notes[i], notes[i + 2], notes[i + 3], notes[i + 5], notes[i + 7], notes[i + 8], notes[i + 10]]
            self.soundscale = [sounds[i], sounds[i + 2], sounds[i + 3], sounds[i + 5], sounds[i + 7], sounds[i + 8],
                               sounds[i + 10]]
            self.symbols = ["I", "ii°", "iii", "IV", "V", "vi", "vii"]
            self.code1 = ""
            self.code2 = "m"
        self.chordscale = []
        self.chordsounds = []
        for x in range(2):
            for a, b in zip(self.scale,self.soundscale):
                self.chordscale.append(a)
                self.chordsounds.append(b)
    def scale_letter(self):
        text = ""
        for e in self.scale:
            text += e + " "
        sclframe.configure(text="Notes of the {} {} Scale".format(self.mynote,self.mytype),fg="#4A235A")
        sclframe.grid(row=0,sticky=W+E)
        Label(sclframe,text="{}{}".format(text, notes[self.i])).grid(row=0,ipadx=30,sticky=E)
    def chord_letter(self):
        chordscale = self.chordscale
        chordframe.configure(text="Chords in the Key of {} {}".format(self.mynote,self.mytype),fg="#D35400")
        chordframe.grid(column=0,row=1,sticky=W+E)
        for e, s in zip(range(7),self.symbols):
            chord = chordscale[e] + " " + chordscale[e+2] + "  " + chordscale[e+4]
            name = chordscale[e]
            if "°" in s:
                name = chordscale[e] + "°"
            elif s.islower():
                name += self.code1
            elif s.isupper():
                name += self.code2
            if " " in name:
                name = name.replace(" ","")
            Label(chordframe,text="{} ({}): ".format(name, s)).grid(ipady=5,column=1,row=e,sticky=E)
            Label(chordframe,text="{}".format(chord)).grid(ipady=5, column=2,row= e,sticky=W)
    def scale_sound(self):
        final = AudioSegment.empty()
        for file in self.soundscale:
            raw = AudioSegment.from_file(file)
            piece = raw[:450].fade_out(450)
            final += piece
        final += AudioSegment.from_file(sounds[self.i + 12]).fade_out(1000)
        final.export("scale.wav", format='wav')
        play(final)
    def chord_sound(self,x):
        first = AudioSegment.from_file(self.chordsounds[x])
        third = AudioSegment.from_file(self.chordsounds[x+2])
        fifth = AudioSegment.from_file(self.chordsounds[x+4])
        com1 = first.overlay(third)
        combined = fifth.overlay(com1).fade_out(1200)
        combined.export("combined.wav", format='wav')
        play(combined)

def control():
    frame0.destroy()
    for widget in sclframe.winfo_children():
        widget.destroy()
    for widget in chordframe.winfo_children():
        widget.destroy()
    Label(chordframe,text=60*" ").grid(row=0,column=0,columnspan=4)
    Label(sclframe, text=60*" ").grid(row=0,column=0, columnspan=4)
    myObject = Key(note.get(),typ.get())
    myObject.scale_letter()
    myObject.chord_letter()
    playbut = Button(sclframe, text="▶ Play Scale ", borderwidth=3, relief="groove", overrelief="sunken"
                     ,bg="#4A235A",fg="#EAEDED",command=myObject.scale_sound,cursor="hand2").grid(row=0,column=5, ipadx=44)
    for x in range(7):
        bg = "#E84300" if x % 2 == 0 else "#EC6E19"
        Button(chordframe, text="▶ Play Chord ", borderwidth=3, relief="groove", overrelief="sunken"
               ,bg=bg,fg="#EAEDED",command=partial(myObject.chord_sound,x),cursor="hand2").grid(row=x, column=5,ipadx=40)
    imgsmall = ImageTk.PhotoImage(Image.open('small.png'))
    img_small = Label(frame2, image=imgsmall,anchor=E)
    img_small.image = imgsmall
    img_small.grid(row=0,column=2,sticky=E,ipadx=30)

notes = ["C ","C♯","D ","E♭","E ","F ","F♯","G ","G♯","A ","B♭","B ","C ","C♯","D ","E♭","E ","F ","F♯","G ","G♯","A ", "B♭", "B "]
notesval = ["C3","Cs3","D3","Ds3","E3","F3","Fs3","G3","Gs3","A3","As3","B3","C4","Cs4","D4","Ds4","E4","F4","Fs4","G4","Gs4","A4", "As4", "B4"]
sounds = ['notes2/' + i + '.wav' for i in notesval]

sclframe = LabelFrame(root,text="hey",pady=10)
frame0 = LabelFrame(root,text="Welcome",pady=10,padx=25,fg="#4A235A")
frame0.grid(row=0)
chordframe = LabelFrame(root,pady=10)
frame1 = LabelFrame(root,text="Choose a note:",padx=130,fg="#4A235A")
frame1.grid(row=2)
frame2 = LabelFrame(root,text="Choose a mode:",padx=5,fg="#D35400")
frame2.grid(row=3,sticky=W+E)

note = StringVar()
note.set("C ")
row = col = 0
for a in notes[:12]:
    radbut = Radiobutton(frame1,text=a,var=note,value=a,borderwidth=3,activeforeground="#4A235A",selectcolor="#D2B4DE",overrelief="groove",cursor="hand2")\
        .grid(row=row,column=col)
    col += 1
    if col == 6:
        row += 1
        col = 0
typ = StringVar()
typ.set("Major")
radbut1 = Radiobutton(frame2,text="Major",var=typ,value="Major",borderwidth=10,anchor=E,activeforeground="#D35400",selectcolor="#E59866",cursor="hand2").grid(row=0,column=0,ipady=10,ipadx=100)
radbut2 = Radiobutton(frame2,text="Minor",var=typ,value="Minor",borderwidth=10,activeforeground="#D35400",selectcolor="#E59866",cursor="hand2").grid(row=0,column=1, ipady=10)

but = Button(root,text="♪  Find Key  ♪",command=control,relief="groove",overrelief="sunken",borderwidth=3
             ,bg="#4A235A",fg="#EAEDED",cursor="hand2").grid(row=4,columnspan=6,ipadx=50,sticky=W+E)

welcome2 = Label(frame0,text="Music Theory Calculator", padx=30,fg="#D35400")
welcome2['font'] = myfont
welcome2.grid(row=1,column=1,ipadx=10)
img0 = ImageTk.PhotoImage(Image.open('Untitled-1.png'))
img_0 = Label(frame0,image=img0,anchor=S).grid(row=0,column=0,columnspan=3,sticky=S,ipady=30)

img1 = ImageTk.PhotoImage(Image.open('wave96.png'))
img_1 = Label(frame0,image=img1).grid(row=1,column=0,sticky=N)

img2 = ImageTk.PhotoImage(Image.open('note96.png'))
img_2 = Label(frame0,image=img2).grid(row=1,column=2,sticky=N)

select = Label(frame0,text="Select a key down below", padx=20,fg="#4A235A",anchor=S).grid(ipady=40,row=2,columnspan=3,sticky=S)
arr = ImageTk.PhotoImage(Image.open("arrow-64.png"))
arrow_label = Label(frame0, image=arr).grid(row=3,column=1)

root.mainloop()
