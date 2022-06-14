from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x500")



main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


mycanvas = Canvas(main_frame)
mycanvas.pack(side=LEFT, fill=BOTH, expand=1)

scr = ttk.Scrollbar(main_frame, orient=VERTICAL, command=mycanvas.yview)
scr.pack(side=RIGHT, fill=Y)

mycanvas.configure(yscrollcommand=scr.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))


frame2 = Frame(mycanvas)

mycanvas.create_window((0,0), window=frame2, anchor="nw")


for i in range(100):
    Label(frame2, text="lorem ipsum").grid(row=i, column=0, padx=10, pady=10)

mainloop()