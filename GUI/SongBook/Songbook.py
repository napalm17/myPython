import requests
import song_pool
from urllib import request, parse
import json
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.font as font
import requests
from tkinter import ttk
from PIL import ImageTk,Image
from PIL import Image
import random as rn


class Song:
    def __init__(self,song_name, artist):
        self.song_name = song_name
        self.artist = artist
    def api_method(self):
        url_api = "https://api.genius.com/"
        url_search = "search?q="
        querystring = url_api + url_search + parse.quote(f"{self.artist} {self.song_name}")
        r = request.Request(querystring)
        r.add_header("Authorization", "Bearer " + "Nc50ScJP_EpICyftwhR0zrP1zXcTf9J1f0Awqd75y9vwsaBlJYbVUHKJP45Vgwhn")
        r.add_header("User-Agent", "")
        response = request.urlopen(r, timeout=3)
        data = json.load(response)
        self.dic = data['response']['hits'][0]['result']
        return self.dic
    def get_image(self):
        image_url = self.dic['header_image_url']
        r = requests.get(image_url)
        with open('song_image.jpg', 'wb') as f:
            f.write(r.content)
    def get_soup(self):
        song_url = self.dic['url']
        source = requests.get(song_url).text
        self.soup = BeautifulSoup(source, 'html.parser')
    def get_lyrics(self):
        self.lyrics = self.soup.find('div', class_='lyrics').text
        return self.lyrics
    def get_album(self):
        self.album_name = self.soup.find('a', class_='song_album-info-title')['title']
        return self.album_name
    def get_year(self):
        year1 = self.soup.find('div', class_='song_body column_layout')
        date = year1.find_all('span', class_='metadata_unit-info metadata_unit-info--text_only')
        for a in date:
            self.year = a.text if "19" or "20" in a.text else "N/A"
        return self.year.split(',')[1][1:]

with open('songlist.txt','r') as f:
    songlist = f.readlines()

song, artist = rn.choice(songlist).split('--')
artist = artist[:-1]
root = Tk()
root.title("Songbook")
myfont = 'Ubuntu'
gen_font = (myfont, 16)
root.option_add('*Font', gen_font)
root.geometry("+200+20")
boldmaker = font.Font(family=myfont, weight="bold", size='14')
big = font.Font(family=myfont, size='18')
small = font.Font(family=myfont, size='14')

frame1 = LabelFrame(root, padx=300, pady=10)
frame1.grid(row=1, columnspan=2)
set_song = StringVar()
set_song.set(song)
entry_song = Entry(frame1,width=25, bg="#D1F2EB", textvariable=set_song)
entry_song.grid(row=0,column=0, padx=0, ipady=5)

by_label = Label(frame1, text="by").grid(row=0, column=1, ipadx=10)

set_artist = StringVar()
set_artist.set(artist)
entry_artist = Entry(frame1,width=25, bg="#D1F2EB", textvariable=set_artist)
entry_artist.grid(row=0,column=2, padx=0, ipady=5)

frame0 = LabelFrame(root, text="Homepage", fg='#117864')
frame0.grid(row=0, sticky=W+E,ipady=200,columnspan=2)
welcome = Label(frame0, text="Welcome to Songbook!\nHere you can find the lyrics of any song you like")
welcome['font'] = big
welcome.pack(expand=1)


def failed_func(song, artist):
    for widget in frame0.winfo_children():
        widget.destroy()
    fail = Label(frame0, text="Couldn't find any song named '{}' by '{}'.".format(song, artist))
    fail.pack(expand=1)

def execute(event):
    try:
        MySong = Song(entry_song.get(), entry_artist.get())
        l = MySong.api_method()
        print(l)
        failed = False
    except:
        failed = True
        failed_func(entry_song.get(),entry_artist.get())
    if not failed:
        new_song = l['title']
        new_artist = l['primary_artist']['name']
        album = "N/A"
        year = ""
        lyrics = ""
        MySong.get_image()
        for i in range(20):
            try:
                MySong.get_soup()
                lyrics = MySong.get_lyrics()
                album = MySong.get_album()
                year = f"({MySong.get_year()})"
                break
            except:
                continue
        frame0.destroy()
        lyr_frame = LabelFrame(root)
        img_frame = LabelFrame(root, text="Album Art", fg="#17A589")
        img_frame.grid(row=0, column=1, sticky=W + E + N + S)
        lyr_frame.configure(text=f'"{new_song}"  by  {new_artist} {year}', pady=10, fg="#117864")
        lyr_frame.grid(row=0, column=0, sticky=W + E + N + S)
        mycanvas = Canvas(lyr_frame)
        mycanvas.grid(sticky=W+E+S+N, column=0,row=0, ipady= 100, ipadx=200)
        scr = ttk.Scrollbar(lyr_frame, orient=VERTICAL, command=mycanvas.yview)
        scr.grid(sticky=N + S, column=1, row=0)
        mycanvas.configure(yscrollcommand=scr.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))
        frame2 = Frame(mycanvas)
        mycanvas.create_window((1000, 500), window=frame2, anchor="nw")
        for line in lyrics.split('\n'):
            lyr = Label(frame2, text=line)
            lyr['font'] = small
            lyr.grid(column=0, padx=20, pady=1, sticky=W)
        brought = Label(frame2,text=3*"-" + "Brought to you by Songbook" + 5000*"-",fg="#117864")
        brought['font'] = small
        brought.grid(column=0)
        global my_img1
        image = Image.open('song_image.jpg')
        image2 = image.resize((500,500), Image.ANTIALIAS)
        my_img1 = ImageTk.PhotoImage(image2)
        my_img2 = Label(img_frame, image=my_img1)
        my_img2.grid(sticky=N + S)

button = Button(frame1,text="Search Song Lyrics",padx=100,bg="#76D7C4",border=1,relief="groove", command=lambda: execute(None), overrelief="sunken",borderwidth=3,cursor="hand2")
button.grid(row=1,columnspan=3, column=0,sticky= W+E, pady=20)

root.bind("<Return>", execute)

mainloop()
