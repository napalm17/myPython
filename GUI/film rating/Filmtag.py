from tkinter import *
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox
from urllib.request import urlopen
import io
import base64
import os
from io import BytesIO
import requests
import json


root = Tk()
#root.iconbitmap('icons8-movie-96 (1).ico')
root.title("Filmtag")
#root.geometry("950x600")
fontm = "Bahnschrift"
my_font = font.Font(family=fontm)
bigfont = font.Font(family=fontm,size=20,weight="bold")
italic = font.Font(family=fontm,slant="italic")
e_font = font.Font(family=fontm,size=14)
title_font = font.Font(family=fontm,weight="bold",underline="yes")
boldmaker = font.Font(family=fontm,weight="bold")

def search():
    for widget in rframe.winfo_children():
        widget.destroy()
    mytitle = ent_title.get()


    try:
        request = requests.get("http://www.omdbapi.com/?t={}&apikey=964d9f6".format(mytitle))
        contents = json.loads((request.content))
        rframe.configure(text=contents['Title'] + " (" + contents['Year'] + ")")
        check = True
    except:
        empty1 = Label(rframe, text="No Film with the title '" + ent_title.get() + "' was found.", padx=240, pady=200,fg="#BB8FCE")
        empty1['font'] = my_font
        empty1.grid(row=0, column=0, ipadx=50)
        check = False

    if check:
        gen_def = Label(rframe, text="Genre: ", fg="#4A235A")

        gen_def['font'] = boldmaker
        gen_def.grid(row=0, column=0, sticky=E)

        gen_label = Label(rframe, text=contents['Genre'])
        gen_label['font'] = my_font
        gen_label.grid(row=0, column=1, sticky=W, columnspan=3)

        dir_def = Label(rframe, text="Director: ", fg="#4A235A")
        dir_def['font'] = boldmaker
        dir_def.grid(row=1, column=0, sticky=E)

        dir_label = Label(rframe, text=contents['Director'])
        dir_label['font'] = my_font
        dir_label.grid(row=1, column=1, sticky=W, columnspan=3)

        cast_def = Label(rframe, text="Cast: ", fg="#4A235A")
        cast_def['font'] = boldmaker
        cast_def.grid(row=2, column=0, sticky=E + N)

        cast_label = Label(rframe, text=contents['Actors'], wraplength=500, justify="left")
        cast_label['font'] = my_font
        cast_label.grid(row=2, column=1, sticky=W + N, columnspan=3)

        plot_def = Label(rframe, text="Plot: ", fg="#4A235A")
        plot_def['font'] = boldmaker
        plot_def.grid(row=3, column=0, sticky=E + N)

        plot_label = Label(rframe, text=contents['Plot'], wraplength=500, justify="left")
        plot_label['font'] = my_font
        plot_label.grid(row=3, column=1, sticky=W + N, columnspan=3)

        award_def = Label(rframe, text="Awards: ", fg="#4A235A")
        award_def['font'] = boldmaker
        award_def.grid(row=4, column=0, sticky=E)

        award_label = Label(rframe, text=contents['Awards'], justify="left")
        award_label['font'] = my_font
        award_label.grid(row=4, column=1, sticky=W, columnspan=3)

        empty = Label(rframe, text="", padx=25)
        empty['font'] = my_font
        empty.grid(row=0, column=5)
        url = urlopen(contents['Poster']).read()
        im = Image.open(BytesIO(url))
        photo = ImageTk.PhotoImage(im)
        img_label = Label(rframe, image=photo, borderwidth=5, relief="groove")
        img_label.image = photo
        img_label.grid(row=0, column=6, rowspan=10)

        rate_def = Label(rframe, text="Ratings: ", fg="#4A235A")
        rate_def['font'] = boldmaker
        rate_def.grid(row=5, column=0, sticky=E)

        try:
            rotten_label = Label(rframe, text=contents['Ratings'][1]['Value'])
            rotten_label['font'] = my_font
            rotten_label.grid(row=5, column=1)

            imdb_img = ImageTk.PhotoImage(Image.open("rotten1 (1).png"))
            imdb_label = Label(rframe, image=imdb_img)
            imdb_label.image = imdb_img
            imdb_label.grid(row=6, column=1)

            imdb_label = Label(rframe, text=contents['Ratings'][0]['Value'])
            imdb_label['font'] = my_font
            imdb_label.grid(row=5, column=2)

            imdb_img = ImageTk.PhotoImage(Image.open("imdb (1).png"))
            imdb_label = Label(rframe, image=imdb_img)
            imdb_label.image = imdb_img
            imdb_label.grid(row=6, column=2)

            meta_label = Label(rframe, text=contents['Ratings'][2]['Value'])
            meta_label['font'] = my_font
            meta_label.grid(row=5, column=3)

            imdb_img = ImageTk.PhotoImage(Image.open("metacritic (1).png"))
            imdb_label = Label(rframe, image=imdb_img)
            imdb_label.image = imdb_img
            imdb_label.grid(row=6, column=3)
        except:
            pass

        img4 = ImageTk.PhotoImage(Image.open('filmtagsmall.png'))
        img_4 = Label(myframe, image=img4, anchor=E)
        img_4.image = img4
        img_4.grid(row=3, column=2, sticky=E, ipadx=75)
    else:
        pass
rframe = LabelFrame(root,padx=10,text="Homepage",fg="#2980B9")
rframe['font'] = my_font
rframe.grid(row=0,column=0)

img0 = ImageTk.PhotoImage(Image.open('filmtag.png'))
img_0 = Label(rframe,image=img0,anchor=S)
img_0.grid(row=0,column=1,ipady=20,sticky=S)


img1 = ImageTk.PhotoImage(Image.open('icons8-film-reel-96.png'))
img_1 = Label(rframe,image=img1)
img_1.grid(row=1,column=0,sticky=N)

empty=Label(rframe,text="Everything you need to know about a movie.\nCondensed.",fg="#4A235A",anchor=N)
empty['font'] = bigfont
empty.grid(row=1,column=1,sticky=N,ipady=40)

img2 = ImageTk.PhotoImage(Image.open('icons8-documentary-96.png'))
img_2 = Label(rframe,image=img2)
img_2.grid(row=1,column=2,sticky=N)



arr = ImageTk.PhotoImage(Image.open("arrowsmallpng.png"))
arrow_label = Label(rframe, image=arr)
arrow_label.grid(row=3,column=1)
empty=Label(rframe,text="Enter the title of the film down below",padx=240,pady=5,fg="#2874A6")
empty['font'] = my_font
empty.grid(row=2,column=0,ipadx=50,columnspan=3)


myframe = LabelFrame(root,pady=10)
myframe.grid(row=1,column=0,sticky=W+E)

label = Label(myframe,text="",padx=120)
label.grid(column=0)


ent_title = Entry(myframe,bg="#E8DAEF")
ent_title['font'] = e_font
ent_title.grid(ipadx=120,ipady=5,column=1)

empty2=Label(myframe,text="",pady=0)
empty2.grid(column=0,ipadx=50)

seach_button = Button(myframe,text="Search by Film Title",command=search,bg="#5DADE2",fg="#4A235A", borderwidth=2, relief="groove", overrelief="sunken")
seach_button['font'] = e_font
seach_button.grid(column=1,ipady=5)

mainloop()
