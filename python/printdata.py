#Printing data to a file using print() function
file = input("Enter a file name   : ")
fh = open(file,"w")
n = int(input("Enter How many rows   : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ",file=fh)
    print(end="\n",file=fh)
fh.close()
fh = open(file,"r")
for line in fh:
    print(line)
fh.close()
