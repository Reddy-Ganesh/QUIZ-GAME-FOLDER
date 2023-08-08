import tkinter as tk
from tkvideo import tkvideo
from tkinter import *

import pygame
import os
import time
w= Tk()
w.title("video")
w.geometry('1920x1080')
w.config(bg="orange")
frame1=Frame(w,width=450,height=450,bg="black",border=0)
frame1.place(x=10,y=20)#presentation1.2
frame2=Frame(w,width=500,height=450,bg="white",border=0)#introductionvideo 

#text1="to start the game you need tho know some this about this game here it "
def get_audio(file1):
    from moviepy.editor import VideoFileClip
    #load the mp4
    video=VideoFileClip(file1+".mp4")
    #extract the audio
    audio=video.audio
    #save the audio as mp3
    audio.write_audiofile(file1+".mp3")
def start(file1):
    global player,lblvideo1
    if not file1+".mp3" in os.listdir("."):
        get_audio(file1)
    pygame.init()
    pygame.mixer_music.load(file1+".mp3")
    lblvideo1=Label(frame1)
    lblvideo1.place(x=10,y=10)
    player=tkvideo(file1+".mp4",lblvideo1,loop=1,size=(420,400))
    player.play()
    pygame.mixer.music.play()
   


def get_audio1(file):
    from moviepy.editor import VideoFileClip
    #load the mp4
    video=VideoFileClip(file+".mp4")
    #extract the audio
    audio=video.audio
    #save the audio as mp3
    audio.write_audiofile(file+".mp3")

text_welcome_home=Label(w,text="WELL-COME TO THE GAME ",width=25,bg="blue",fg="white",border=0,font=("Microsoft Yahei UI Light",23))
text_welcome_home.place(x=550,y=20)
def frame1_krishna():
    
    #here the frame1 postion was chnaged
    frame1.place_configure(x=10,y=350)
    frame2.place(x=400,y=150)
    start_krishna_video1("mainframevideo2")

    
    

def start_krishna_video1(file):
    
    
    
    if not file+".mp3" in os.listdir("."):
        get_audio1(file)
    pygame.init()
    pygame.mixer_music.load(file+".mp3")
    
    lblvideo2=Label(frame2)
    lblvideo2.place(x=10,y=10)
    player1=tkvideo(file+".mp4",lblvideo2,loop=1,size=(350,350))
    player1.play()
    pygame.mixer.music.play()
    

button1=Button(frame1,text="start",bg="green",fg="white",command=frame1_krishna)

button1.place(x=150,y=420)




start("presentation1.2")


frame3=Frame(w,width=675,height=675,bg="black",border=0)#to play inmroduction of ramayanan

def introduction_to_story(file1):
    from moviepy.editor import VideoFileClip
    #load the mp4
    video=VideoFileClip(file1+".mp4")
    #extract the audio
    audio=video.audio
    #save the audio as mp3
    audio.write_audiofile(file1+".mp3")
def start_intodution_rama(file1):
   
    if not file1+".mp3" in os.listdir("."):
        introduction_to_story(file1)
    pygame.init()
    pygame.mixer_music.load(file1+".mp3")
    lblvideo3=Label(frame3)
    lblvideo3.place(x=20,y=10)
    player2=tkvideo(file1+".mp4",lblvideo3,loop=1,size=(625,625))
    player2.play()
    pygame.mixer.music.play()
    

#rama story intoduction-------------------------------------

def frame3_introduction_rama():
    
    pygame.mixer.music.stop()
    
    frame1.destroy()
    w.config(bg="black")
    frame2.place_configure(x=5,y=250)

    
# here the frame3 placed on the window(w)
    frame3.place(x=550,y=80)
    start_intodution_rama("mainframevideo1")

    
    


button2=Button(frame2,text="see the into",bg="green",fg="white",command=frame3_introduction_rama)

button2.place(x=220,y=425)


    

def rama_story_delete():
    pygame.mixer.music.stop()
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    text_welcome_home.destroy()
    w.destroy()
    # Here we import the another file(second.py) we import windows1(tk)
    from second import windows1 
    import second

    
button3=Button(frame3,text="skip",bg="green",fg="white",command=rama_story_delete)
button3.place(x=275,y=650)






w.mainloop()