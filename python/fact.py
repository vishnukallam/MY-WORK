num = int(input("enter number:\n"))
fact = 1
for i in range(1,num+1):
	if i <= num:
		fact = fact * i
		print(fact)
	else:
		print("the fact is not possible")