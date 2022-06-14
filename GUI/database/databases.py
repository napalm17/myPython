from tkinter import *
import tkinter.font as font
import sqlite3

root = Tk()
root.geometry('720x300')
root.title("Database")
myfont = font.Font(family="Futura")
under = font.Font(underline="yes")
boldmaker = font.Font(weight="bold",underline="yes")

'''
connect = sqlite3.connect('Favorite Music.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE fav_music (
                rock_album text,
                rock_artist text,
                rock_song text,
                jazz_album text,
                jazz_artist text,
                jazz_song text,
                rap_album text,
                rap_artist text,
                rap_song text
                )
                """)

connect.commit()
connect.close()
'''

def submit():
    connect = sqlite3.connect('Favorite Music.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO fav_music VALUES (:rock_album, :rock_artist, :rock_song, :jazz_album, :jazz_artist, :jazz_song, :rap_album, :rap_artist, :rap_song)",
                    {
                        'rock_album': rock_album.get(),
                        'rock_artist': rock_artist.get(),
                        'rock_song': rock_song.get(),
                        'jazz_album': jazz_album.get(),
                        'jazz_artist': jazz_artist.get(),
                        'jazz_song': jazz_song.get(),
                        'rap_album': rap_album.get(),
                        'rap_artist': rap_artist.get(),
                        'rap_song': rap_song.get()
                    })


    connect.commit()
    connect.close()

    rock_album.delete(0, END)
    rock_artist.delete(0, END)
    rock_song.delete(0, END)
    jazz_album.delete(0, END)
    jazz_artist.delete(0, END)
    jazz_song.delete(0, END)
    rap_album.delete(0, END)
    rap_artist.delete(0, END)
    rap_song.delete(0, END)

def query():
    connect = sqlite3.connect('Favorite Music.db')
    cursor = connect.cursor()
    cursor.execute("SELECT *, oid FROM fav_music")
    recs = cursor.fetchall()
    print_rec = ""
    for rec in recs:
        print_rec += str(rec[0])+ " " + str(rec[3])+ " " +str(rec[6]) + " " + str(rec[9]) +"\n"
    top = Toplevel()
    top.geometry('500x500')
    qry_lbl = Label(top,text=print_rec)
    qry_lbl.grid(row=0,column=0)
    connect.commit()
    connect.close()

def delete():
    connect = sqlite3.connect('Favorite Music.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM fav_music WHERE oid= " + ent_del.get())

    connect.commit()
    connect.close()
def edit():
    top = Tk()
    top.geometry('720x300')
    top.title("Edit Record")
    lbl_genre = Label(top, text="Genre", anchor=E)
    lbl_rock = Label(top, text="Rock:", anchor=E)
    lbl_jazz = Label(top, text="Jazz:", anchor=E)
    lbl_rap = Label(top, text="Rap:", anchor=E)

    lbl_genre['font'] = myfont
    lbl_genre['font'] = boldmaker

    lbl_rock['font'] = myfont
    lbl_jazz['font'] = myfont
    lbl_rap['font'] = myfont

    lbl_genre.grid(row=0, column=0, ipadx=10)
    lbl_rock.grid(row=1, column=0, ipadx=10)
    lbl_jazz.grid(row=2, column=0, ipadx=10)
    lbl_rap.grid(row=3, column=0, ipadx=10)

    lbl_album = Label(top, text="Your favorite Album")
    lbl_artist = Label(top, text="Your favorite Artist")
    lbl_song = Label(top, text="Your favorite Song")

    lbl_album['font'] = myfont
    lbl_artist['font'] = myfont
    lbl_song['font'] = myfont
    lbl_album['font'] = under
    lbl_artist['font'] = under
    lbl_song['font'] = under

    lbl_album.grid(row=0, column=1)
    lbl_artist.grid(row=0, column=2)
    lbl_song.grid(row=0, column=3)
    a = 30
    rock_album = Entry(top, borderwidth=2, width=a, bg="#D7C0C0")
    rock_artist = Entry(top, borderwidth=2, width=a, bg="#D7C0C0")
    rock_song = Entry(top, borderwidth=2, width=a, bg="#D7C0C0")
    jazz_album = Entry(top, borderwidth=2, width=a, bg="#AFDBF5")
    jazz_artist = Entry(top, borderwidth=2, width=a, bg="#AFDBF5")
    jazz_song = Entry(top, borderwidth=2, width=a, bg="#AFDBF5")
    rap_album = Entry(top, borderwidth=2, width=a, bg='#D0F0C0')
    rap_artist = Entry(top, borderwidth=2, width=a, bg='#D0F0C0')
    rap_song = Entry(top, borderwidth=2, width=a, bg='#D0F0C0')

    rock_album.grid(row=1, column=1)
    rock_artist.grid(row=1, column=2)
    rock_song.grid(row=1, column=3)
    jazz_album.grid(row=2, column=1)
    jazz_artist.grid(row=2, column=2)
    jazz_song.grid(row=2, column=3)
    rap_album.grid(row=3, column=1)
    rap_artist.grid(row=3, column=2)
    rap_song.grid(row=3, column=3)
    save_button = Button(top, text="Save changes", bg="#9EF2FF", command=edit, border=1, padx=20)
    save_button['font'] = myfont
    save_button.grid(row=4, column=2)


button = Button(root,text="Submit",bg="#BCFF90",command=submit,border=1,padx=60)
button['font'] = myfont
button.grid(row=4,column=1)

qry_button = Button(root,text="Show Records",bg="#9EF2FF",command=query,border=1,padx=20)
qry_button['font'] = myfont
qry_button.grid(row=4,column=2)

qry_button = Button(root,text="Delete Record",bg="#F97A7A",command=delete,border=1,padx=20)
qry_button['font'] = myfont
qry_button.grid(row=7,column=1)

lbl_delete = Label(root,text="Select ID:")
lbl_delete['font'] = myfont
lbl_delete.grid(row=5,column=0,ipadx=50)

up_button = Button(root,text="Update Record",bg="gray",command=edit,border=1,padx=20)
up_button['font'] = myfont
up_button.grid(row=6,column=1)

ent_del = Entry(root,borderwidth=2,width=5,bg="#FFB4B4")
ent_del.grid(row=5,column=1)


lbl_genre = Label(root,text="Genre",anchor=E)
lbl_rock = Label(root,text="Rock:",anchor=E)
lbl_jazz = Label(root,text="Jazz:",anchor=E)
lbl_rap = Label(root,text="Rap:",anchor=E)


lbl_genre['font'] = myfont
lbl_genre['font'] = boldmaker

lbl_rock['font'] = myfont
lbl_jazz['font'] = myfont
lbl_rap['font'] = myfont


lbl_genre.grid(row=0,column=0,ipadx=10)
lbl_rock.grid(row=1,column=0,ipadx=10)
lbl_jazz.grid(row=2,column=0,ipadx=10)
lbl_rap.grid(row=3,column=0,ipadx=10)

lbl_album = Label(root,text="Your favorite Album")
lbl_artist = Label(root,text="Your favorite Artist")
lbl_song = Label(root,text="Your favorite Song")

lbl_album['font'] = myfont
lbl_artist['font'] = myfont
lbl_song['font'] = myfont
lbl_album['font'] = under
lbl_artist['font'] = under
lbl_song['font'] = under

lbl_album.grid(row=0,column=1)
lbl_artist.grid(row=0,column=2)
lbl_song.grid(row=0,column=3)
a = 30
rock_album = Entry(root,borderwidth=2,width=a,bg="#D7C0C0")
rock_artist = Entry(root,borderwidth=2,width=a,bg="#D7C0C0")
rock_song = Entry(root,borderwidth=2,width=a,bg="#D7C0C0")
jazz_album = Entry(root,borderwidth=2,width=a,bg="#AFDBF5")
jazz_artist = Entry(root,borderwidth=2,width=a,bg="#AFDBF5")
jazz_song = Entry(root,borderwidth=2,width=a,bg="#AFDBF5")
rap_album = Entry(root,borderwidth=2,width=a,bg='#D0F0C0')
rap_artist = Entry(root,borderwidth=2,width=a,bg='#D0F0C0')
rap_song = Entry(root,borderwidth=2,width=a,bg='#D0F0C0')

rock_album.grid(row=1,column=1)
rock_artist.grid(row=1,column=2)
rock_song.grid(row=1,column=3)
jazz_album.grid(row=2,column=1)
jazz_artist.grid(row=2,column=2)
jazz_song.grid(row=2,column=3)
rap_album.grid(row=3,column=1)
rap_artist.grid(row=3,column=2)
rap_song.grid(row=3,column=3)




root.mainloop()