'''from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.title('File dialog')
filename=askopenfilename(initialdir='/',filetypes=[('All files', '.*'),('All files', '*')])
s=open(filename).read()
textbox = ScrolledText()
textbox.grid()
textbox.insert(1.0,s)
mainloop()
'''
import sys
x = 10
print(sys.getsizeof(x))