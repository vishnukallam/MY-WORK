import tkinter
from tkinter import *
class okquit:
    def __init__(self):
        self.window=Tk()
        self.window.title('OK & QUIT DEMO')
        self.window.geometry('400x400')
        self.text=Entry(self.window,width=15)
        self.text.pack()
        self.lbl=Label(self.window,text="",font=('Ariel Bold',16))
        self.lbl.pack()
        self.btnok=Button(self.window,text="OK",command=self.clickok)
        self.btnok.pack()
        self.btnquit=Button(self.window,text="QUIT",command=self.clickquit)
        self.btnquit.pack()
        self.window.mainloop()
    def clickok(self):
        if len(self.text.get()) == 0:
            message="Please Enter Data"
            self.lbl.configure(text=message)
        else:
            print(self.text.get())
            self.text.delete(0,END)
    def clickquit(self):
        self.window.destroy()
okquit()