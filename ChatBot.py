from tkinter import*
from tkinter import colorchooser




win=Tk()
win.geometry('400x590+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')
win.config(bg="#ececec")

#--Image Add--
image = PhotoImage(file="chatbot-1.png")
Label(win, image=image).place(x=-215,y=0)

def color():
    cl=colorchooser.askcolor()

def dark():
    win.config(bg="#262626")
    la1.config(bg="#262626",fg="#F5F5F5")
    la2.config(bg="#262626",fg="#F5F5F5")
    la3.config(bg="#262626",fg="#F5F5F5")
    la4.config(bg="#262626",fg="#F5F5F5")
    r1.config(bg="#262626",fg="#F5F5F5")
    r2.config(bg="#262626",fg="#F5F5F5")

def light():
    win.config(bg="#ececec")
    la1.config(bg="#ececec",fg="black")
    la2.config(bg="#ececec",fg="black")
    la3.config(bg="#ececec",fg="black")
    la4.config(bg="#ececec",fg="black")
    r1.config(bg="#ececec",fg="black")
    r2.config(bg="#ececec",fg="black")




#--Welcome to pikachu chatbot--
la1=Label(win,text="Welcome to Pikachu",font=('veranda',25,''),bg="#ececec")
la1.place(x=50,y=320)

la2=Label(win,text="ChatBot",font=('veranda',25,''),bg="#ececec")
la2.place(x=140,y=360)

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

but2=Button(win,text="Enter",width=10,font=('calibri',11,''),bg="#2E8B57",fg="white")
but2.place(x=160,y=540)




win.mainloop()