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
import wikipedia
import time
import requests


#--Main Windows--
win=Tk()
win.geometry('400x590+400+15')
win.title("Pikachu VoiceBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')
win.config(bg="#ececec")

#--Enter Voice-Bot--

def chat_enter():


    r = sp.Recognizer()

    def record_audio(ask=False):

        with sp.Microphone() as source:
            if ask:
                pikachu_speak(ask)
            audio = r.record(source,duration=3)
            text = ''

            try:
                text = r.recognize_google(audio)

            except sp.UnknownValueError:
                pikachu_speak("Sorry I did not get that")

            except sp.RequestError:
                pikachu_speak("Sorry, my speech service is down")
        return text

    def pikachu_speak(audio_string):
        adio=gTTS(text=audio_string,lang='en')
        ran=random.randint(1,10000000)
        audio_file='audio-'+str(ran)+'.mp3'
        adio.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)


    def respond(voice_or_text_data):


        if 'what is your name' in voice_or_text_data :
            fr1=Frame(frm1,bg=color)
            fr1.place(x=0,y=0,height=590,width=400)

            chat=Label(fr1,text="My name is pikachu.\nI am a bot.I work for you",bg="#FA8072",font=('calibri',12,''))
            chat.place(x=5,y=50)

            pikachu_speak("My name is pikachu. I am a bot. I work for you")

        elif 'how are you' in voice_or_text_data:
            fr1 = Frame(frm1,bg=color)
            fr1.place(x=0,y=0,height=590,width=400)

            chat = Label(fr1,text="I am fine. Nice to talk with you",bg="#FA8072",font=('calibri',12,''))
            chat.place(x=5,y=50)

            pikachu_speak("I am fine. Nice to talk with you")

        elif 'what time is it now' in voice_or_text_data:
            fr1 = Frame(frm1,bg=color)
            fr1.place(x=0,y=0,height=590,width=400)

            chat = Label(fr1,text="Current Local time.\n"+ctime(),bg="#FA8072",font=('calibri',12,''))
            chat.place(x=5,y=50)

            pikachu_speak("Current Local Time:")
            pikachu_speak(ctime())

        elif "search" in voice_or_text_data:
            fr1 = Frame(frm1,bg=color)
            fr1.place(x=0,y=0,height=590,width=400)

            search = record_audio("what do you want to search for?")

            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)

            chat1 = Label(fr1,text="Here is search:",bg="#3CB371",font=('calibri',12,''))
            chat1.place(x=5,y=110)

            pikachu_speak("here is search" + search)

        elif 'find location' in voice_or_text_data:
            location = record_audio("Say the name of the location?")
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            pikachu_speak("The location:")

        elif 'Wikipedia' in voice_or_text_data:
            wiki=record_audio("what do you want to search in wikipedia?")

            try:
                pikachu_speak(wikipedia.summary(wiki,sentences=3))
            except:
                pikachu_speak("Not found")
        elif 'weather' in voice_or_text_data:

            location=record_audio("Say the name of the location:")
            link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=c4c80c6387c03dde649323ba4e878114"
            api_link = requests.get(link)
            api_data = api_link.json()

            #Store data
            city = ((api_data['main']['temp']) - 273.15)
            weather = api_data['weather'][0]['description']
            humadity = api_data['main']['humidity']
            wind_speed = api_data['wind']['speed']

            if api_data['cod']=='404':
                pikachu_speak("Incorrect location name.Please check the location")
            else:
                temp=float("{:.2f}".format(city))
                pikachu_speak("Current temperature is: "+str(temp)+" degree Celsius")
                pikachu_speak("Weather forecast :" + weather)
                pikachu_speak("Humidity :" +str( humadity)+" percentage")
                pikachu_speak("Wind speed :" + str(wind_speed) + 'kilometre per hour')

        else:
            pikachu_speak("I am a pikachu chatbot")



    def ri():
        voice_data = record_audio()
        respond(voice_data)



    global cl
    global var
    color = "";bg_clr1="";mode = "";fg_clr1="";bg_clr2="";fg_clr2="";ac1=""
    select_value = var.get()

    if select_value == 1:
        color = "#262626";mode = "#808080";bg_clr1="#262626";fg_clr1="#C0C0C0";bg_clr2="#696969";fg_clr2="white";ac1="#d1d0c6"
    if select_value == 2:
        color = "#ececec";mode = "#C0C0C0";bg_clr1="#2E8B57";fg_clr1="#F8F8FF";bg_clr2="#625f3e";fg_clr2="white";ac1="#A3A18E"

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

    frmi=Frame(bg=color)
    frmi.place(x=0,y=0,height=590,width=400)

    frm1=Frame(frmi,bg=color)
    frm1.place(x=0,y=0,height=500,width=400)

    frm2=Frame(frmi,bg=mode)
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
        bu2 = Button(frm2,relief=RAISED,image=img2,command=ri)
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
        bu2 = Button(frm2,relief=RAISED,image=img2,command=ri)
        bu2.image = img2
        bu2.place(x=25,y=25,height=34,width=20)




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

    la2 = Label(fr1,text="VoiceBot",font=('veranda',25,''),bg="#ececec")
    la2.place(x=130,y=360)

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


    la4 = Label(fr1,text="Background",font=('calibri',11,''),bg="#ececec")
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

    la2 = Label(fr1,text="VoiceBot",font=('veranda',25,''),bg="#262626",fg="#F5F5F5")
    la2.place(x=130,y=360)

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

    la4 = Label(fr1,text="Background",font=('calibri',11,''),bg="#262626",fg="#F5F5F5")
    la4.place(x=50,y=490)
    but1 = Button(fr1,text="Pick Color",width=20,font=('calibri',10,''),bg="#878f84",fg="white",command=color)
    but1.place(x=190,y=490)

    # --Enter to the chat--
    but2 = Button(fr1,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white",command=chat_enter)
    but2.place(x=160,y=540)


light()
win.mainloop()
