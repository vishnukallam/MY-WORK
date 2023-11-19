import random
		#print list
		#----------
list_0 = []
for i in range(1,20):
	list_0.append(random.randint(1,100))
print(list_0)
		#sum and avarage of list
		#-----------------------
x = sum(list_0)
y = len(list_0)
avarage = x/y
print(avarage)
print(x)
		#printing max and min value in list
		#----------------------------------
print(str(max(list_0)),",",str(min(list_0)))
		#print second largest and second smallest element in the list
		#------------------------------------------------------------
for i in range(1,20):
	list_1=sorted(list_0)
print(list_1)
print("the second smallest number in list is",list_1[1])
print("the second largest number in list is",list_1[-2])
		#printing the even number
		#------------------------
for x in (list_1):
	if x%2==0:
		print(x,end=',')

	