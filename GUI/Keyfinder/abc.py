import Tkinter, Pmw, os, sys

def makeGUI(top):
    Tkinter.Label(text='Demonstration of\nfont and color options').pack(pady=5)
    list = Pmw.ScrolledListBox(top,
           label_text = 'my first Pwm widget',
           labelpos = 'n')
    list.pack(pady=5)
    Tkinter.Button(top, text='button 1').pack(pady=5)
    Tkinter.Button(top, text='button 2').pack(pady=5)

    mylist = ('item1','item2','item3')
    for item in mylist:
        list.insert('end', item)

def readOptions():
    if not os.path.isfile('.tkoptions'):
        print 'no file .tkoptions in the current directory'
        return
    global root
    root.option_readfile('.tkoptions')

def addOptions():
    general_font = ('Helvetica', 14, 'bold')
    label_font = ('Times', 24, 'italic')
    listbox_font = ('Helvetica', 20, 'roman bold')

    # check which fonts that are actually available:
    import tkFont
    print 'label_font:',label_font,'\n  realized as',\
          tkFont.Font(font=label_font).actual()
    print 'general_font:',general_font,'\n  realized as',\
          tkFont.Font(font=general_font).actual()
    print 'listbox_font:',listbox_font,'\n  realized as',\
          tkFont.Font(font=listbox_font).actual()

    global root
    root.option_add('*Font', general_font)
    root.option_add('*Foreground', 'black')
    root.option_add('*Label*Font', label_font)
    root.option_add('*Listbox*Font', listbox_font)
    root.option_add('*Listbox*Background', 'green')
    root.option_add('*Listbox*Foreground', 'brown')

root = Tkinter.Tk()
try:
    if sys.argv[1] == 'file':
        readOptions()
    else:
        addOptions()
except:
    print 'fonts.py file|add'; sys.exit(1)

Pmw.initialise(root,useTkOptionDb=1)

root.title('demonstrating font and color settings')

makeGUI(root)
root.mainloop()