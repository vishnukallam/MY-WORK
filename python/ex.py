# #import keyword
# # print(keyword.kwlist)
# # import random
# # x= random.randint(1,10)
# # y=int(input("enter any number b/w 1,10:\n"))
# # if y<=10:
# # 	print(y,'exist')
# # else:
# # 	print(y,'not exist')
# # a = float(input('enter a value:\n'))
# # b = float(input('enter b value:\n'))
# # z = abs(a-b)
# # if z <= 0.01:
# # 	print(z,'close')
# # else:
# # 	print(z,'not close')
# # word = 'aeip'
# # vowels = 'aeiouAEIOU'
# # for i in word:
# # 	if i in vowels:
# # 		print(word,'vowels are there')
# # 	else:
# # 		print(word,'no vowels')
# # s1 = input('s1:\n')
# # s2 = input('s2:\n')
# # if len(s1) == len(s2):
# # 	for i in range(len(s2)):
# # 		print(s2[i],s1[i],sep='',end='')
# # a=input("enter an expression:")
# # s=a[0]
# # for i in range(1,len(a)):
# # 	if(a[i].isalpha() and a[i-1].isdigit() or a[i]=='(' or a[i].isalpha() and a[i-1].isalpha() or a[i-1]==')' or a[i].isdigit() and a[i-1].isalpha()):
# # 		s=s+"*"
# # 	s=s+a[i]
# # print(f"expression is :{s}")
# # n=int(input("Enter any integer:"))
# # a=[i for i in range(1,n+1) if n%i==0]  
# # print(f"Factors of {n} in the list are {a}")
# # from tkinter import *
# # from tkinter.filedialog import *
# # from tkinter.scrolledtext import ScrolledText
# # root = Tk()
# # root.title('File dialog')
# # filename=askopenfilename(initialdir='/',filetypes=[('All files', '.*'),('All files', '*')])
# # s=open(filename).read()
# # textbox = ScrolledText()
# # textbox.grid()
# # textbox.insert(1.0,s)
# # mainloop()
# # print(dir())
# # class revstr:
# #     def reverse_words(self, s):
# #         return ' '.join(reversed(s.split()))
# # print(revstr().reverse_words(input("enter any string: ")))
# # def fd(s,d):
# #     a=min(len(s),len(d))
# #     for i in range(a):
# #         if s[i]!=d[i]:
# #             return i+1
# #     return a if len(s)!=len(d) else -1
# # s=input("Enter 1:")
# # d=input("Enter 2:")
# # print(fd(s,d))
# # class helo:
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def add(self):
# #         print(f"the addition {self.a+self.b}")
# # class hi (helo):
# #     def __init__(self,a,b,c,d):
# #         super().__init__(a,b)
# #         super().add()
# #         self.c=c
# #         self.d=d
# #     def sub(self):
# #         print(f"the subration {self.c-self.d}")
# # hello = hi(1,2,3,4)
# # hello.sub() 
# # class node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.ref= None
# # class list:
# #     def __init__(self):
# #         self.head = None
# #     def printlist(self):
# #         if self.head is None:
# #             print("The list empty")
# #         else:
# #             n = self.head
# #             while n is not None:
# #                 print(f'{n.data}->',end='')
# #                 n=n.ref
# #     def addnode(self,data):
# #         new_node = node(data)
# #         new_node.ref = self.head
# #         self.head = new_node
# # ll = list()
# # for i in range(1,10+1):
# #     ll.addnode(i)
# # ll.printlist()
# # def check_pass_fail(mark):
# #     if mark >= 40:
# #         return "Pass"
# #     else:
# #         return "Fail"
# # mark = int(input("Enter the subject mark: "))

# # result = check_pass_fail(mark)

# # print(result)
# '''class employee:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self.dept=dept
#         self.salary=salary
#     def display(self):
#         print(f"The name of the employee {self.name} \nDepartment {self.dept} \nSalary {self.salary}")
# n,d,s="vishnu","CSE",20000
# Emp=employee(n,d,s)
# Emp.display()'''
# def count_vowels(word):
#     vowel_count = 0
#     letter_count = len(word)
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     for char in word:
#         if char.lower() in vowels:
#             vowel_count += 1

#     vowel_percentage = (vowel_count / letter_count) * 100

#     return {
#         'letter_count': letter_count,
#         'vowel_count': vowel_count,
#         'vowel_percentage': vowel_percentage
#     }

# # Read the word from the user
# word = input("Enter a word: ")

# # Call the function to count letters and vowels
# result = count_vowels(word)

# # Print the results
# print("Number of letters:", result['letter_count'])
# print("Number of vowels:", result['vowel_count'])
# print("Percentage of vowels:", result['vowel_percentage'], "%")

v = input
print(list(v))