from logging import root
from tkinter import *
from pygame.locals import *
from PIL import ImageTk, Image
from playsound import playsound
import os
from pygame import mixer


co1 ="white"
co2 = "#3C1DC6"
co3 = "black"
co4 = "pink"


window = Tk()
window.title("ZASS MUSIC PLAYER")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)


def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    
    show()

    listbox.select_set(new_index)
    running_song['text'] = playing


def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing


left_frame = Frame(window, width=150, height=150,bg=co1)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame = Frame(window, width=250, height=150, bg=co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=400, height=100, bg=co4)
down_frame.grid(row=1, column=0, columnspan=3,padx=0,pady=1)
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 9 bold"), width=22,bg=co3,fg=co1)
listbox.grid(row=0,column=0)


w = Scrollbar(right_frame,bg=co1)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

img_1 = Image.open('img/img1.png')
img_1 = img_1.resize((100,100))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image=img_1,padx=10 , bg=co1)
app_image.place(x=24,y=15)

img_2 = Image.open('img/play1.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=30,height=32, image=img_2,padx=10 , bg=co1,font=("Ivy 10"), command=play_music)
play_button.place(x=60+28,y=40)

img_3 = Image.open('img/pause1.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
pause_button = Button(down_frame, width=30,height=30, image=img_3,padx=10 , bg=co1,font=("Ivy 10"), command = pause_music)
pause_button.place(x=150+28,y=40)

img_4 = Image.open('img/stop1.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
stop_button = Button(down_frame, width=30,height=30, image=img_4,padx=10 , bg=co1,font=("Ivy 10"),command=stop_music)
stop_button.place(x=240+28,y=40)

img_5= Image.open('img/forward2.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
front_button = Button(down_frame, width=30,height=30, image=img_5,padx=10 , bg=co1,font=("Ivy 10"),command=previous_music)
front_button.place(x=15+28,y=40)

img_6= Image.open('img/forward1.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
back_button = Button(down_frame, width=30,height=30, image=img_6,padx=10 , bg=co1,font=("Ivy 10"),command=next_music)
back_button.place(x=105+28,y=40)

img_7= Image.open('img/preview1.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
continue_button = Button(down_frame, width=30,height=30, image=img_7,padx=10 , bg=co1,font=("Ivy 10"),command=continue_music)
continue_button.place(x=195+28,y=40)

line = Label(left_frame,width= 201, height=1, padx=10 , bg=co3)
line.place(x=0,y=1)

line = Label(left_frame,width= 200, height=1, padx=10 , bg=co1)
line.place(x=0,y=3)

running_song = Label(down_frame, text="Choose a song",font=("Ivy 10"), width=44, height=1, padx=10, bg=co1,fg=co3)
running_song.place(x=0,y=1)

os.chdir(r'C:\Users\laksh\Desktop\create mp3 player using python\music')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()
