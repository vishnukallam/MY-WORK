'''def print_factors(x):
   print("The factors of",int(x),"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i,end='  ')
num = int(input("enter any number"))
print_factors(num)'''
def is_sorted(l):
    flag = 1
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            flag = 0
            break
    if flag ==1:
        return True
    else:
        return False
x =[]
y=int(input('enter size of a list'))
for i in range(y):
    z = int(input("enter values"))
    x.append(z)
print(f"The list is {x}")
print(f"The list is sorted{is_sorted(x)}")