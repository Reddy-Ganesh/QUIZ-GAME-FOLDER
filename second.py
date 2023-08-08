from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import time
import pygame
from tkvideo import tkvideo



windows1=Tk()
windows1.geometry('1920x1080')
windows1.title("Funny quiz")
windows1.config(bg="orange")
pygame.init()
#here the game musics is start.......
pygame.mixer_music.load(filename="audio.mp3")
pygame.mixer_music.play()
# here we the volume to high if it is 1.0 high and 0.5 it is average
pygame.mixer_music.set_volume(1.0)
#img4,picture1.inside the exam page
# image5,pic are in  sign page 

s=PhotoImage(file="img4.png")
t=PhotoImage(file="Picture1.png")
image1=Label(windows1,image=s,border=0)
image2=Label(windows1,image=t,border=0)
main_image1=PhotoImage(file="image5.png")
main_image2=PhotoImage(file="pic.png")
image3=Label(windows1,image=main_image1,border=0,bg="black")
image4=Label(windows1,image=main_image2)

image3.place(x=20,y=150)
image4.place(x=550,y=500)

#frame1 for sign page
#frame2  exam frame it was placed in exam() line 

frame2=Frame(windows1,width=750,height=500,)

             

frame1=Frame(windows1,bg="white",border=1,width=350,height=600)


frame1.place(x=1050,y=80)

#text for introduction it was place in frame3
#here fraem3 was place in the signin page
text1=["Welcome to the Quiz! Test your knowledge and challenge",
       ",yourself with a series of exciting questions.",
">To participate, you must sign in using your email ID.",
">The quiz is designed to be challenging.",
">So think carefully before answering each question.",
">There is no option to go back to the previous question.",
">Once you have proceeded to the next one.",
">Try to answer as accurately as possible.",
">And see how well you perform compared to others.",
">Feel free to take the quzi",
"***BE COOL BE HAPPY***",
"***ENJOY THE LIFE"]


frame3=Frame(windows1,width=500,height=450,border=5,bg="#39254D")
frame3.place(x=370,y=50)
t1=Label(frame3,text="NOTE",bg='black',fg="#12674a",font=('Castellar',16,'bold'))
t1.place(x=150,y=40)
# her for loop to place the text1 in frame3 line by line
for i in range(len(text1)):
    
    y_position=(90+(i*30))
    t3=Label(frame3,text=text1[i],bg="#39254D",fg="#D4AF37",font=("Times New Roman",14))
    t3.place(x=40,y=y_position)


def exam():
    global name1,email1
    name1=name.get()
    email1=email.get()
    name1,email1=str(name1),str(email1)
    if len(name1)>3 and len(email1)>10:
        frame3.destroy()
        image3.destroy()
        image4.destroy()
        frame1.destroy()
        windows1.config(bg="black")
        frame2.place(x=10,y=90)
        image1.place(x=850,y=50)
        #image2.place(x=870,y=650)
        
        
    else:
        messagebox.showerror('OPPS!', 'please enter both the fields')

#label to show to on sign in option
Label(frame1,text="Enter to quiz",border=0,bg='black',fg="#57a1f8",font=('Microsoft Yahei UI Light',23,'bold')).place(x=30,y=35)
def on_enter(e):
    name.delete(0,'end')
def on_leave(e):
    if name.get()=='':
        name.insert(0,"name")

name =Entry(frame1,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
name.place(x=30,y=150)
name.insert(0,'name')
name.bind("<FocusIn>",on_enter)
name.bind("<FocusOut>",on_leave)
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=177)

def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    if email.get()=='':
        email.insert(0,"email")
email=Entry(frame1,width=25,bg="white",fg="black",border=0,font=("Microsoft Yahei UI Light",11))
email.place(x=30,y=220)
email.insert(0,"email")
email.bind("<FocusIn>",on_enter)
email.bind("<FocusOut>",on_leave)
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=245)


x=Button(frame1,text="Enter to exam",bg="green",font=("Microsoft Yahei UI Light",11),command=exam)
x.place(x=70,y=270)



question=[
    {
    "q":"Who is the younger brother of Lord Rama?",
    "option":["Bharata","Lakshmana","Shatrughna","Hanuman"],
    "correct":"B) Lakshmana"
},
{
    "q":"What is the name of Lord Rama's loyal charioteer during the war against Ravana",
    "option":["Sushena","Sugriva","Vibhishana","Hanuman"],
    "correct":"Hanuman"
},

{"q":"Who is Sita's adoptive father?",
"option":["King Janaka","King Dasharatha","Sage Valmiki","Lord Brahma"],
"correct": "King Janaka"
},
{"q":"What is the name of Lord Rama's bow?",
 "option":["Agni-astra","Pashupatastra","Brahmastra","Sharanga"],
"correct": "Sharanga"},
{"q":"How many years did Lord Rama, Sita, and Lakshmana spend in exile in the forest?",
 "option":["10 years","12 years","14 years","16 years"],
"correct": "14 years"},
{
"q":"Who is the main protagonist in the Ramayana?",
"option":["Hanuman","Ravana","Sita","Lord Rama"],
"correct":"Lord Rama"
},
{
"q":"Which demon king kidnaps Sita and takes her to Lanka?",
"option":["Kumbhakarna","Vibhishana","Ravana","Maricha"],
"correct":"Ravana"
}
]

    



option=tk.StringVar()

st=[]
#t is declear as list to plrin the question numbers
t=[] 
for i in range(1,len(question)+1):
    t.append(str(i))

y=len(question)+1
for i in range(1,y+1):
    t.append(str(i))
#okay method is use print the questions in the tkinter framework
def okay():
    
    global question_no,x,t,score
    score=0

    
    x=len(question)
    question_no=0
    label_question_no.config(text=str(t[question_no])+""+"/"+str(x))
    label_question.config(text=question[question_no]["q"])
    for i, option in enumerate(question[question_no]["option"]):
        option_buttons[i].config(text=option, variable=selected_option, value=option)




        
selected_option=tk.StringVar()
#next method is used to print question on by on and give the output in after all question was finished
def next():
    
    global question_no,score,name2,t,x
    
    
    

    selected = selected_option.get()
    correct_answer = question[question_no]["correct"]

    if selected == correct_answer:
        score += 1

    question_no += 1

    if question_no <len(question):
        label_question_no.config(text=str(t[question_no])+""+"/"+str(x))
        
        label_question.config(text=question[question_no]["q"])

        for i, option in enumerate(question[question_no]["option"]):
            option_buttons[i].config(text=option, variable=selected_option, value=option)
    else:
        
        pygame.mixer_music.stop()
        name2=str(name1)
        windows1.config(bg="#B0C4DE")
        image1.destroy()
        image2.destroy()
        frame2.destroy()
        frame_result.place(x=10,y=20)
        frame_result_video.place(x=350,y=190)
        y=Label(frame_result,text="Thanks for Playing",font=('Microsoft Yahei UI Light',18,'bold'))
        y.place(x=10,y=60)
        z=Label(frame_result,text=""+str(name2),font=("Times New Roman",23))
        z.place(x=10,y=10)
        x = tk.Label(frame_result, text="Quiz Completed. Your Score: " + str(score) + "/" + str(len(question)),font=('Microsoft Yahei UI Light',16,'bold'))
        x.place(x=10,y=100)
        frame_result_MESSAGE.place(x=920,y=10)
        start("endvideo")
        text1=["In this game, you may skip or leave some questions,",
               "just as in your life, you may face and try to escape or skip some problems",
               "However, here you need to know that if you leave a problem unresolved,",
                "you can't go back to the same time to solve it.",
                "So take your time and solve your problems which ocuur in ourlife", "Also, there is no previous button in our game.","BE HAPPY BE COOL","ENJOY THE LIFE"]
        for i in range(len(text1)):
            y_position=(50+(i*30))
            t3=Label(frame_result_MESSAGE,text=text1[i],fg="#D4AF37",font=("Times New Roman",14))
            t3.place(x=20,y=y_position)

       




    




       
# Option radiobuttons
option_buttons = []

for i in range(4):
    y1=50 + i * 60
    radio_btn = tk.Radiobutton(frame2, text="", variable=selected_option, value="", font=("Arial", 12))
    option_buttons.append(radio_btn)
    radio_btn.place(x=20,y=y1)

def get_audio(file1):
    from moviepy.editor import VideoFileClip
    #load the mp4
    video=VideoFileClip(file1+".mp4")
    #extract the audio
    audio=video.audio
    #save the audio as mp3
    audio.write_audiofile(file1+".mp3")
def start(file1):
    global player
    if not file1+".mp3" in os.listdir("."):
        get_audio(file1)
    pygame.init()
    pygame.mixer_music.load(file1+".mp3")
    label_end=Label(frame_result_video)
    label_end.place(x=5,y=5)
    player=tkvideo(file1+".mp4",label_end,loop=1,size=(550,550))
    player.play()
    pygame.mixer.music.play()
    pygame.mixer.music.rewind()

    
   
useranswer=tk.StringVar()


# Question label
label_question = tk.Label(frame2, text="",font=("Arial", 14))
label_question.place(x=10,y=30)
label_question_no=tk.Label(frame2,text="",font=("Arial",14))
label_question_no.place(x=500,y=10)


frame_result=Frame(windows1,width=450,height=170)
frame_result_MESSAGE=Frame(windows1,width=590,height=300,bg="orange")
frame_result_video=Frame(windows1,width=570,height=570,bg="black")

next1=Button(frame2,text="next",bg="green",fg="white",command=next)
next1.place(x=350,y=350)




okay()
windows1.mainloop()