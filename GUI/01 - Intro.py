from tkinter import *
root = Tk()

root.geometry("500x500")
root.configure(bg="black")
button_quit = Button(root,text="Exit now!",command=root.quit)
button_quit.grid(row=10,column=0)

ent = Entry(root,fg="black",bg="gray",width=50,borderwidth=5)
ent.grid(row=0,column=0)
ent.insert(0,"Don't enter anything: ")
def click():
    string = "Did you really have to type " + ent.get().upper() +"?"
    #my_label1 = Label(root, text="the sun is a deadly laser",fg="orange", bg="red")
    #my_label1.grid(row=3, column=0)
    my_input = Label(root, text=string, fg="orange", bg="red")
    my_input.grid(row=5, column=0)

#my_label2 = Label(root, text="not anymore, there is a blanket")
my_button = Button(root,text="don't click",padx=10,pady=10,command=click,fg="cyan",bg="black")
#my_label2.grid(row=1, column=0)
my_button.grid(row=3,column=0)

root.mainloop()