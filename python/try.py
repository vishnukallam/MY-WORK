"""x=int(input("enter a number:"))
print(f"{x:,}")"""
#import random
#l =[]
#for i in range(1,20):
#    l.append(random.randint(1,100))
#print(l) 
#print(f'''the sum of list is {sum(l)}\nthe average of list is {sum(l)/len(l)}the largest value amoung the list is {str(max(l))}
#the smallest value amooung the list is {str(min(l))}''')
#l1= sorted(l)
#print(l1)
#print(f"""the second largest in the list{l1[-2]}\n the second smallest inthe list {l1[2]}""")
#for i in l1:
#    if i %2 == 0:
#        print([i],end='')
'''n=int(input(""))
l=[]
for i in range(1,n+1):
    if n % i == 0:
        l.append(i)
print(l)'''
'''import random
random_integers = [random.randint(0, 1) for _ in range(100)]
max_zeros = 0
current_zeros = 0
for num in random_integers:
    if num == 0:
        current_zeros += 1
        max_zeros = max(max_zeros, current_zeros)
        print(max_zeros,end="  ")
    else:
        current_zeros = 0

print("Random Integers:", random_integers)
print("Longest run of zeros:", max_zeros)'''
#########17,15###########
def srings(s1,s2):
    if s1==s2:
        return -1
    else:
        for i in range(min(len(s1),len(s2))):
            if s1[i]!=s2[i]:
                return i+1
    print(f"the first different at {i+1}")
s1='vishnu'
s2='Vishn'
x = srings(s1,s2)
if x==-1:
    print(f"the strings are equal")
else:
    print("not equal")