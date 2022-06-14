from tkinter import *
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("Calculator")
#root.iconbitmap(r'calculator.ico')
x = 30
y = 20
fg = "White"
bg = "#1B2631"
fg1 = "White"
bg1 = "#2C3E50"
root.configure(bg="#1C2833")

e = Entry(root, width=10, borderwidth=3, bg="#85929E")
myfont = font.Font(family="Helvetica Bold")
inputfont = font.Font(size=24)
e['font'] = myfont
e['font'] = inputfont
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def click_button(num):
    var = e.get()
    e.delete(0, END)
    e.insert(0, str(var) + str(num))
def clear_button():
    e.delete(0, END)
def op_button(op):
    global op1
    op1 = op
    global num_1
    num_1 = float(e.get())
    e.delete(0, END)
def calc():
    try:
        num_2 = float(e.get())
        e.delete(0, END)
        ops1 = ["+", "-", "*", "/"]
        ops2 = [num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2]
        for i, x in zip(ops1, ops2):
            if i == op1:

                e.insert(0, round(x,2))
                break
    except:
        messagebox.showerror(ZeroDivisionError,"Can't divide value by zero!")


button_add = Button(root, text="+", padx=x, pady=y, command=lambda: op_button("+"), fg=fg1, bg=bg1,relief="groove",overrelief="sunken")
button_add['font'] = myfont
button_sub = Button(root, text="−", padx=x, pady=y, command=lambda: op_button("-"), fg=fg1, bg=bg1,relief="groove",overrelief="sunken")
button_sub['font'] = myfont
button_mul = Button(root, text="×", padx=x, pady=y, command=lambda: op_button("*"), fg=fg1, bg=bg1,relief="groove",overrelief="sunken")
button_mul['font'] = myfont
button_div = Button(root, text="÷", padx=x, pady=y, command=lambda: op_button("/"), fg=fg1, bg=bg1,relief="groove",overrelief="sunken")
button_div['font'] = myfont
button_clean = Button(root, text="C", padx=29, pady=y, command=clear_button, fg=fg, bg="#78281F",relief="groove",overrelief="sunken")
button_clean['font'] = myfont
button_equ = Button(root, text="=", padx=29, pady=y, command=lambda: calc(), fg=fg, bg="#0B5345",relief="groove",overrelief="sunken")
button_equ['font'] = myfont
button1 = Button(root, text="1", padx=x, pady=y, command=lambda: click_button(1), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button1['font'] = myfont
button2 = Button(root, text="2", padx=x, pady=y, command=lambda: click_button(2), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button2['font'] = myfont
button3 = Button(root, text="3", padx=x, pady=y, command=lambda: click_button(3), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button3['font'] = myfont
button4 = Button(root, text="4", padx=x, pady=y, command=lambda: click_button(4), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button4['font'] = myfont
button5 = Button(root, text="5", padx=x, pady=y, command=lambda: click_button(5), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button5['font'] = myfont
button6 = Button(root, text="6", padx=x, pady=y, command=lambda: click_button(6), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button6['font'] = myfont
button7 = Button(root, text="7", padx=x, pady=y, command=lambda: click_button(7), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button7['font'] = myfont
button8 = Button(root, text="8", padx=x, pady=y, command=lambda: click_button(8), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button8['font'] = myfont
button9 = Button(root, text="9", padx=x, pady=y, command=lambda: click_button(9), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button9['font'] = myfont
button0 = Button(root, text="0", padx=x, pady=y, command=lambda: click_button(0), fg=fg, bg=bg,relief="groove",overrelief="sunken")
button0['font'] = myfont
button_clean.grid(row=4, column=0)
button0.grid(row=4, column=1)
button_equ.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

root.mainloop()

