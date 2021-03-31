from tkinter import*




win=Tk()
win.geometry('400x550+400+15')
win.title("Pikachu ChatBot")
win.resizable(False,False)
win.iconbitmap(r'chabot.ico')

image = PhotoImage(file="chatbot-1.png")
Label(win, image=image).place(x=-215,y=0)



win.mainloop()