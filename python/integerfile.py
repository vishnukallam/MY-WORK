#write 100 random integers to a file
#find the sum and average of integers from the file
import random
file = input("Enter a file name   : ")
fh = open(file,"w")
for i in range(100):
    n = random.randint(1,100)
    fh.write(str(n)+"\n")
fh.close()
fh = open(file,"r")
s = 0
for line in fh:
    line = line.strip()
    n = int(line)
    s = s + n
a = s / 100.0
print("Sum of all integers in the file is  :",s)
print("Average of all integers in the file is  :",a)
