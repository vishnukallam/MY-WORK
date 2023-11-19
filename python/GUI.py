# # from tkinter import *
# # window = Tk()
# # window.title('Hello')
# # window.geometry('600x600')
# # label=Label(window,text='Welcome to The World',font=('Times Roman',20))
# # label.grid(column = 20,row = 5)
# # window.mainloop()
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")
# except Exception as e:
    # print("Error:", e)
# Factorial of a number using recursion

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = int(input("enetr"))
# print(recur_factorial(num))
class family:
    def __init__(self,father,mother):
        self.father = father
        self.mother = mother
    def display(self):
        print(self.father,' ',self.mother)
class sons(family):
    def sonname(self, father, mother,son):
        super().__init__(father, mother)
        self.son = son
    def display(self):
        super().display()
        print(self.son)
f1=sons('raksh','anu','hersha')
print(f1.son)
