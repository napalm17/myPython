from tkinter import *
from tkinter import  ttk, colorchooser
import pyscreenshot as ImageGrab
root = Tk()

class Main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'white'
        self.color_bg = 'black'
        self.old_x = None
        self.old_y = None
        self.penwidth = 40
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg, capstyle=ROUND, smooth=True)
        self.old_x = e.x
        self.old_y = e.y
    def reset(self, e):
        self.old_x = None
        self.old_y = None
    def changeW(self, e):
        self.penwidth = e
    def clear(self):
        self.c.delete(ALL)
    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]
    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def get_ss(self, widget):
        x = root.winfo_rootx() + widget.winfo_x()
        y = root.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        im = ImageGrab.grab(bbox=(x, y, x1, y1))
        im.save('screenshot.png')
    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width').grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeW, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=100)
        self.controls.pack(side=BOTTOM)
        self.c = Canvas(self.master, width = 500, height=500, bg=self.color_bg)
        self.c.pack(fill=BOTH, expand=True)
        self.but = Button(self.controls, text="Save", command=lambda: self.get_ss(self.c))
        self.but.grid(row=1, column=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)


Main(root)
root.mainloop()