'''from tkinter import *
from PIL import ImageTk, Iamge

root = Tk()
root.geometry('700x500')
root.title('STUDENTS REGISTRATIONS FORM')

# main heading 
label1 = Label(text="Ramachandra College Of Engineering")
label1.config(font=('Arial bold ',30),bg='red')
#label1.grid(row=0, column=0,padx=15,pady=15 )
label1.grid(row=0, column=0, ipadx=15, ipady=15)

# profile photo
img = Image.open('images(7).jpeg')
img = img.resize((14,14))
img = ImageTk.photImage(img)
label2 = Label(image=img)
label2.grid(row=1, column=0)

root.mainloop()check,radio,cambo,massege'''
from tkinter import *
window = Tk()
window.title('"THE WINDOW"')
window.geometry('1180x1180')
#label1
l=Label(text='Name:',font=('Times New Roman',20))
l.grid(column=1,row=2)
#entry1
entry= Entry(window,font=('Times New Roman',20))
entry.grid(column=3,row=2)
#label2
l=Label(text='Dept.:',font=('Times New Roman',20))
l.grid(column=1,row=4)
#entry2
entry0=Entry(window,font=('Times New Roman',20))
entry0.grid(column =3 , row = 4)
#Btton1
hello1 = Button(window,text="SUBMIT",bg='red',fg='white',width='10')
hello1.grid(column=3,row=8)
#Button2
hello = Button(window,text="CLEAR",bg='orange',fg='white',width='10')
hello.grid(column=3,row=10)
window.mainloop()
