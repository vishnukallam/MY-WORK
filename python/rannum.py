# import random
# r= random.randint(1,10+1)
# print(r)
# s=0
# while True:
#     x = int(input('enter any number : '))
#     if x==r:
#         print(x)
#         break
#     s=s+1 
# print(f"your random number is equal at {s} iteration")
string = '12345'
sum= 0
for i in string:
    print(i)
sum += int(i)
print(sum)