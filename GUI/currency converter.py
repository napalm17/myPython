from tkinter import *
import tkinter.font as font
import requests
from tkinter import ttk

root = Tk()

root.title("Currency Converter")
general_font = ('Cambria', 20)
root.option_add("*Font", general_font)
myfont = font.Font(size="50",family= "Cambria")
small = font.Font(size="1",family= "Cambria")
url = 'https://api.exchangerate-api.com/v4/latest/USD'

data = requests.get(url).json()
currencies = data['rates']

def makeBase(input, amount):
    for x in currencies:
        if x == input:
            based = amount / float(currencies[x])
            return based
def convert(inputCur, amount, outputCur):
    if inputCur != "USD":
        amount = makeBase(inputCur, amount)
    for x in currencies:
        if x == outputCur:
            outputAmount = amount * currencies[x]
            return outputAmount
def execute():
    result = convert(inputCur.get(), float(amountEnt.get()), outputCur.get())
    result2 = str(round(result, 3))
    out.configure(text=result2, padx= 20)

list = []
for i in currencies:
    list.append(i)

heading = Label(root, text=20*"-" + "Currency--Converter" + 20*"-", pady=10, fg="#154360")
heading.grid()
mainframe= LabelFrame(root)
mainframe.grid()

amountEnt = Entry(mainframe,borderwidth=2,width=10,bg="#D4E6F1")
amountEnt.grid(row=0, column=0)

arrow = Label(mainframe,text="⇄", padx=10, fg="#154360")
arrow.grid(row=0,column=2)
arrow['font'] = myfont

out = Label(mainframe,text="         ", padx=50)
out.grid(row=0,column=3)

var1 = StringVar(mainframe)
var1.set(list[0])

var2 = StringVar(mainframe)
var2.set(list[47])

inputCur = ttk.Combobox(mainframe, textvariable=var1, values=list, width=4)
inputCur.grid(row=0, column=1)

outputCur = ttk.Combobox(mainframe, textvariable=var2, values=list, width=4)
outputCur.grid(row=0, column=4)

button = Button(mainframe,text="Convert",padx=10,bg="#A9CCE3",border=1,command=execute,relief="groove")
button.grid(row=2,columnspan=5, column=0,sticky=W+E)

sm = Label(mainframe)
sm['font'] = small
sm.grid(row=1,columnspan=5, column=0, ipadx=300)
mainloop()