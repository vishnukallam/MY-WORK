
n = int(input('enter any value:\n'))
List = []
for i in range(1,n+1):
	if n %i == 0: 
		List.append(i)
print("the factor of given ",n, "is ",List)


'''number_of_stars_USA = int(input("Enter the row's value for diamond"))   
for m in range(0,number_of_stars_USA):
    for n in range(0,number_of_stars_USA-m-1):
        print(" ",end='')
    for l in range(0,2*m+1):
        print("*",end='')
    print()
for m in range(number_of_stars_USA-1,0,-1):
    for n in range(number_of_stars_USA,m,-1):
        print(" ",end='')
    for l in range(2*m-1,0,-1):
        print("*",end='')
    print() '''
'''n= int(input("Enter the row's value for diamond"))  
for m in range(0,n):
    for n in range(0,n-m-1):
        print(" ",end='')
    for l in range(0,2*m+1):
        print("*",end='')
    print()'''
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()