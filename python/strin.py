s1 = input("enter string")
s2 = input("enter string")
if len(s1) == len(s2):
    for i in range (len(s1)):
        print(s2[i],s1[i],sep='',end='')
else:
    print("not equal")
