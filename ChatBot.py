from tkinter import*
from tkinter import colorchooser
from PIL import ImageTk,Image


#--Main Windows--
win=Tk()
win.geometry('400x590+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')
win.config(bg="#ececec")

#--Enter Chat-Bot--
def chat_enter():
    global cl
    global var
    color = ""
    mode = ""
    select_value = var.get()

    if select_value == 1:
        color = "#262626"
        mode = "#262626"
    if select_value == 2:
        color = "#ececec"
        mode = "#ececec"
    cnt=0
    try:
       for i in cl:
           cnt = cnt + 1
           if cnt == 2:
               color = i
    except:
        print("")

    frm1=Frame(bg=color)
    frm1.place(x=0,y=0,height=590,width=400)

    frm2=Frame(frm1,bg="yellow")
    frm2.place(x=0,y=510,height=80,width=400)

    bu=Button(frm2,command=home)
    bu.place(x=0,y=0)

def home():

    # --Change into Light Mode--
    def light():
        fr1.config(bg="#ececec")
        la1.config(bg="#ececec",fg="black")
        la2.config(bg="#ececec",fg="black")
        la3.config(bg="#ececec",fg="black")
        la4.config(bg="#ececec",fg="black")
        r1.config(bg="#ececec",fg="black")
        r2.config(bg="#ececec",fg="black")

        photo2 = ImageTk.PhotoImage(Image.open("chatbot-1.png"))
        p.config(image=photo2)
        p.photo_ref = photo2

    # --Change into Dark Mode--
    def dark():
        fr1.config(bg="#262626")
        la1.config(bg="#262626",fg="#F5F5F5")
        la2.config(bg="#262626",fg="#F5F5F5")
        la3.config(bg="#262626",fg="#F5F5F5")
        la4.config(bg="#262626",fg="#F5F5F5")
        r1.config(bg="#262626",fg="#F5F5F5")
        r2.config(bg="#262626",fg="#F5F5F5")

        photo2 = ImageTk.PhotoImage(Image.open("chatbot-2.jpg"))
        p.config(image=photo2)
        p.photo_ref = photo2

    # --Color Palette--
    def color():
        global cl
        cl = colorchooser.askcolor()

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
    r1 = Radiobutton(fr1,text="Dark",variable=var,value="1",bg="#ececec",command=dark)
    r1.place(x=190,y=450)
    r2 = Radiobutton(fr1,text="Light",variable=var,value="2",bg="#ececec",command=light)
    r2.place(x=290,y=450)


    la4 = Label(fr1,text="Chat Background",font=('calibri',11,''),bg="#ececec")
    la4.place(x=50,y=490)
    but1 = Button(fr1,text="Pick Color",width=20,font=('calibri',10,''),bg="#878f84",fg="white",command=color)
    but1.place(x=190,y=490)

    # --Enter to the chat--
    but2 = Button(fr1,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white",command=chat_enter)
    but2.place(x=160,y=540)

home()
win.mainloop()
