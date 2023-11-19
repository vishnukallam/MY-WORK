#Printing data to a file using print() function
file = input("Enter a file name   : ")
fh = open(file,"w")
n = int(input("Enter How many rows   : "))
for i in range(1,n+1):
    x = input()
    print(x+"\n",end=" ",file=fh)
fh.close()
print("The contents of the file is....")
fh = open(file,"r")
for line in fh:
    print(line)
fh.close()
