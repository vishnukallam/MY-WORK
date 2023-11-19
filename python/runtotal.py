'''x = int(input('enter x value:'))
binary = ''
while x!=0:
    r = x%2
    binary = str(r)+binary
    x= x//2
print(binary)'''
'''s= 0 
while True:
    x= input('enter value of x : ')
    if x == '':
        break
    s = s+int(x)
print(s)'''
x,s = int(input('enter x value')),0 
for i in range(x+1):
    if i % 2 ==0:
        print(i)
        s=s+i
print(s)

'''x =int(input(''))
y =int(input())
print(id(x))
print(id(y))'''
'''x= 10
l =[1,2,3,4,x,10]
print(l[4])'''
# s= 0 
# while True:
#     x= input('enter value of x : ')
#     if x == '':
#         break
#     s = s+int(x)
# print(s)
# #binary  
# x = int(input('enter x value:'))
# binary = ''
# while x!=0:
#     r = x%2
#     binary = str(r)+binary
#     x= x//2
# print(binary)
# print(bin(10))