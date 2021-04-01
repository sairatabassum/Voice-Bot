from tkinter import*
from tkinter import colorchooser
from PIL import ImageTk,Image



win=Tk()
win.geometry('400x590+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')
win.config(bg="#ececec")

#--Image Add--
image = PhotoImage(file="chatbot-1.png")
p=Label(win, image=image)
p.place(x=-215,y=0)

def color():
    cl=colorchooser.askcolor()

#--Change into Dark Mode--
def dark():
    win.config(bg="#262626")
    la1.config(bg="#262626",fg="#F5F5F5")
    la2.config(bg="#262626",fg="#F5F5F5")
    la3.config(bg="#262626",fg="#F5F5F5")
    la4.config(bg="#262626",fg="#F5F5F5")
    r1.config(bg="#262626",fg="#F5F5F5")
    r2.config(bg="#262626",fg="#F5F5F5")


    photo2 = ImageTk.PhotoImage(Image.open("chatbot-2.jpg"))
    p.config(image=photo2)
    p.photo_ref = photo2

#--Change into Light Mode--
def light():
    win.config(bg="#ececec")
    la1.config(bg="#ececec",fg="black")
    la2.config(bg="#ececec",fg="black")
    la3.config(bg="#ececec",fg="black")
    la4.config(bg="#ececec",fg="black")
    r1.config(bg="#ececec",fg="black")
    r2.config(bg="#ececec",fg="black")


    photo2 = ImageTk.PhotoImage(Image.open("chatbot-1.png"))
    p.config(image=photo2)
    p.photo_ref = photo2

def chat_enter():
    print(var.get())


#--Welcome to pikachu chatbot--
la1=Label(win,text="Welcome to Pikachu",font=('veranda',25,''),bg="#ececec")
la1.place(x=50,y=310)

la2=Label(win,text="ChatBot",font=('veranda',25,''),bg="#ececec")
la2.place(x=140,y=360)

#--Theme & Chat background--
la3=Label(win,text="Theme",font=('calibri',11,''),bg="#ececec")
la3.place(x=50,y=450)

var=IntVar()
var.set("2")
r1=Radiobutton(win,text="Dark",variable=var,value=1,command=dark,bg="#ececec")
r1.place(x=190,y=450)
r2=Radiobutton(win,text="Light",variable=var,value=2,command=light,bg="#ececec")
r2.place(x=290,y=450)



la4=Label(win,text="Chat Background",font=('calibri',11,''),bg="#ececec")
la4.place(x=50,y=490)
but1=Button(win,text="Pick Color",command=color,width=20,font=('calibri',10,''),bg="#878f84",fg="white")
but1.place(x=190,y=490)

#--Enter to the chat--
but2=Button(win,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white",command=chat_enter)
but2.place(x=160,y=540)




win.mainloop()