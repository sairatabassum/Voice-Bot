from tkinter import*
from tkinter import colorchooser
from PIL import ImageTk,Image
import speech_recognition as sp
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import time


#--Main Windows--
win=Tk()
win.geometry('400x590+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')
win.config(bg="#ececec")

#--Enter Chat-Bot--
def chat_enter():
    def pikachu_speak(audio_string):
        adio=gTTS(text=audio_string,lang='en')
        ran=random.randint(1,10000000)
        audio_file='audio-'+str(ran)+'.mp3'
        adio.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)


    def respond(voice_and_text_data):
        print(voice_and_text_data)


    global cl
    global var
    color = "";bg_clr1="";mode = "";fg_clr1="";bg_clr2="";fg_clr2=""
    select_value = var.get()

    if select_value == 1:
        color = "#262626";mode = "#808080";bg_clr1="#262626";fg_clr1="#C0C0C0";bg_clr2="#696969";fg_clr2="white"
    if select_value == 2:
        color = "#ececec";mode = "#C0C0C0";bg_clr1="#2E8B57";fg_clr1="#F8F8FF";bg_clr2="#625f3e";fg_clr2="white"

    cnt = 0
    clp = ""
    try:
        for i in cl:
            cnt = cnt + 1
            if cnt == 2:
                clp = i
    except:
        print(" ")

    if clp != None and clp != "":
        color = clp

    frm1=Frame(bg=color)
    frm1.place(x=0,y=0,height=590,width=400)

    frm2=Frame(frm1,bg=mode)
    frm2.place(x=0,y=500,height=90,width=400)

    if select_value==1:
        im=Image.open("setting.png")
        n=im.resize((48,48))
        img=ImageTk.PhotoImage(n)
        bu=Button(frm2,command=dark,relief=FLAT,image=img)
        bu.image=img
        bu.place(x=360,y=28,height=30,width=30)

        im2 = Image.open("gramophone-record.png")
        n2 = im2.resize((60,60))
        img2 = ImageTk.PhotoImage(n2)
        bu2 = Button(frm2,relief=FLAT,image=img2)
        bu2.image = img2
        bu2.place(x=15,y=25,height=30,width=30)

    elif select_value==2:
        im=Image.open("green-settings.png")
        n=im.resize((40,40))
        img=ImageTk.PhotoImage(n)
        bu = Button(frm2,relief=FLAT,command=light,image=img)
        bu.image=img
        bu.place(x=360,y=28,height=30,width=30)

        im2 = Image.open("record.png")
        n2 = im2.resize((55,55))
        img2 = ImageTk.PhotoImage(n2)
        bu2 = Button(frm2,relief=FLAT,image=img2)
        bu2.image = img2
        bu2.place(x=25,y=25,height=34,width=20)


    txt=StringVar()
    en1=Entry(frm2,textvariable=txt,font=('Arial',15,'bold'),bg=bg_clr1,fg=fg_clr1)
    en1.place(x=60,y=22,height=40,width=220)
    en1.insert(0,"Text Something...")

    b3=Button(frm2,text="Send",font=('calibri',11),bg=bg_clr2,fg=fg_clr2,command=lambda: respond(en1.get()))
    b3.place(x=290,y=22,height=40,width=50)



# --Color Palette--
def color():
    global cl
    cl = colorchooser.askcolor()

# --Change into Light Mode--
def light():

    fr1=Frame(win,bg="#ececec")
    fr1.place(x=0,y=0,width=400,height=590)

    # --Image Add--
    image = ImageTk.PhotoImage(Image.open("chatbot-1.png"))
    p = Label(fr1,image=image)
    p.image=image
    p.place(x=-215,y=0)

    # --Welcome to pikachu chatbot--
    la1 = Label(fr1,text="Welcome to Pikachu",font=('veranda',25,''),bg="#ececec")
    la1.place(x=50,y=310)

    la2 = Label(fr1,text="ChatBot",font=('veranda',25,''),bg="#ececec")
    la2.place(x=140,y=360)

    # --Theme & Chat background--
    la3 = Label(fr1,text="Theme",font=('calibri',11,''),bg="#ececec")
    la3.place(x=50,y=450)

    global var
    var = IntVar()
    var.set("2")
    r1 = Radiobutton(fr1,text="Dark",variable=var,value=1,bg="#ececec",command=dark)
    r1.place(x=190,y=450)
    r2 = Radiobutton(fr1,text="Light",variable=var,value=2,bg="#ececec",command=light)
    r2.place(x=290,y=450)


    la4 = Label(fr1,text="Chat Background",font=('calibri',11,''),bg="#ececec")
    la4.place(x=50,y=490)
    but1 = Button(fr1,text="Pick Color",width=20,font=('calibri',10,''),bg="#878f84",fg="white",command=color)
    but1.place(x=190,y=490)

    # --Enter to the chat--
    but2 = Button(fr1,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white",command=chat_enter)
    but2.place(x=160,y=540)


# --Change into Dark Mode--
def dark():
    fr1 = Frame(win,bg="#262626")
    fr1.place(x=0,y=0,width=400,height=590)

    # --Image Add--
    image = ImageTk.PhotoImage(Image.open("chatbot-2.jpg"))
    p = Label(fr1,image=image)
    p.image = image
    p.place(x=-215,y=0)

    # --Welcome to pikachu chatbot--
    la1 = Label(fr1,text="Welcome to Pikachu",font=('veranda',25,''),bg="#262626",fg="#F5F5F5")
    la1.place(x=50,y=310)

    la2 = Label(fr1,text="ChatBot",font=('veranda',25,''),bg="#262626",fg="#F5F5F5")
    la2.place(x=140,y=360)

    # --Theme & Chat background--
    la3 = Label(fr1,text="Theme",font=('calibri',11,''),bg="#262626",fg="#F5F5F5")
    la3.place(x=50,y=450)

    global var
    var = IntVar()
    var.set("1")
    r1 = Radiobutton(fr1,text="Dark",variable=var,value=1,bg="#262626",fg="#F5F5F5",command=dark)
    r1.place(x=190,y=450)
    r2 = Radiobutton(fr1,text="Light",variable=var,value=2,bg="#262626",fg="#F5F5F5",command=light)
    r2.place(x=290,y=450)

    la4 = Label(fr1,text="Chat Background",font=('calibri',11,''),bg="#262626",fg="#F5F5F5")
    la4.place(x=50,y=490)
    but1 = Button(fr1,text="Pick Color",width=20,font=('calibri',10,''),bg="#878f84",fg="white",command=color)
    but1.place(x=190,y=490)

    # --Enter to the chat--
    but2 = Button(fr1,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white",command=chat_enter)
    but2.place(x=160,y=540)


light()
win.mainloop()
