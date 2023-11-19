import tkinter
from tkinter import *
class okquit:
    def __init__(self):
        self.window=Tk()
        self.window.title="ok quit demo"
        self.window.geometry('200x200')
        self.entry= Entry(self.window,width=20)
        self.entry.pack()
        self.label=Label(self.window,text="",font=("Times New Roman",15))
        self.label.pack()
        self.button=Button(self.window,text="Ok",font=("Times New Roman",10),command=self.clickok)
        self.button.pack()
        self.button1=Button(self.window,text="Quit",font=("Times New Roman",10),command=self.clickquit)
        self.button1.pack()
        self.window.mainloop()
    def clickok(self):
        if len(self.entry.get()) == 0:
            message = "enter any text"
            self.label.configure(text=message)
        else:
            print(self.entry.get())
            self.entry.delete(0,END)
    def clickquit(self):
        self.window.destroy()
okquit()
