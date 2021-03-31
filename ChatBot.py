from tkinter import*




win=Tk()
win.geometry('400x580+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')

image = PhotoImage(file="chatbot-1.png")
Label(win, image=image).place(x=-215,y=0)

la1=Label(win,text="Welcome to Pikachu",font=('veranda',25,''))
la1.place(x=50,y=300)


la2=Label(win,text="ChatBot",font=('veranda',25,''))
la2.place(x=140,y=350)



win.mainloop()