from tkinter import *
#import csv  # Data sheet
#from PIL import ImageTk, Image  # for reading an image


def func():
    f = open('students.csv', 'a')
    roll_ = entry3.get().upper()
    name_ = entry1.get().title()
    branch_ = entry2.get().upper()

    '''csvwriter = csv.writer(f)
    csvwriter.writerow([roll_, name_, branch_])
    f.close()'''

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


root = Tk()
root.geometry('700x500')
root.title('STUDENT REGISTRATION FORM')


frame1 = Frame(root)
# Main heading  creation
label1 = Label(frame1, text='Ramachandra College Of Engineering, Eluru')
label1.config(font=('Arial Rounded MT Bold', 23), bg='red')
label1.grid(row=0, column=0, ipadx=15, ipady=15)
# Roll number
frame2 = Frame(root)
roll = Label(frame2, text='Roll :', font=('Arial Rounded MT Bold', 20))
roll.grid(row=2, column=0, ipadx=30, ipady=15)
entry3 = Entry(frame2, width=30, font=('Arial Rounded MT Bold', 20))
entry3.grid(row=2, column=1)

# Name
name = Label(frame2, text='Name :', font=('Arial Rounded MT Bold', 20))
name.grid(row=3, column=0, ipadx=30)
entry1 = Entry(frame2, width=30, font=('Arial Rounded MT Bold', 20))
entry1.grid(row=3, column=1)

# Branch
branch = Label(frame2, text='Branch :', font=('Arial Rounded MT Bold', 20))
branch.grid(row=4, column=0, ipadx=30, ipady=15)
entry2 = Entry(frame2, width=30, font=('Arial Rounded MT Bold', 20))
entry2.grid(row=4, column=1)

button1 = Button(frame2, text='Submit', font=('Arial Rounded MT Bold', 20))
button1.config(bg='green', command=lambda: func())
button1.grid(row=5, column=0, columnspan=30)

frame2.pack()

root.mainloop()
