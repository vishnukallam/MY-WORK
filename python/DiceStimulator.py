import random
while next!="exit":
    num=random.randint(1,6)
    if num==1:
        print(" ____________")
        print("|            |")
        print("|            |")
        print("|     0      |")
        print("|            |")  
        print("|____________|")
    elif num==2:
        print(" ____________")
        print("|            |")
        print("|            |")
        print("|  0     0   |")
        print("|            |")
        print("|____________|")
    elif num==3:
        print(" ____________")
        print("|            |")
        print("|            |")
        print("|  0     0   |")
        print("|     0      |")
        print("|____________|")
    elif num==4:
        print(" ____________")
        print("|            |")
        print("|            |")
        print("|   0    0   |")
        print("|   0    0   |")
        print("|____________|")
    elif num==5:
        print(" ____________")
        print("|            |")
        print("|  0    0    |")
        print("|    0       |")
        print("|  0    0    |")
        print("|____________|")
    elif num==6:
        print(" ____________")
        print("|            |")
        print("|  0    0    |")
        print("|  0    0    |")
        print("|  0    0    |")
        print("|____________|")
    if next=="exit":
        break
    next=input("To roll again press enter")
