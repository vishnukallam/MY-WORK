import random
def repetedElement(a,n):
    while True:
        i = random.randint(1,100) % n+1
        j = random.randint(1,100) % n+1
        print(i)
        print(j)
        if i != j and a[i] == a[j]:
            return i

a = [10,20,30,40,50,60,60,60,60,60]
k = repetedElement(a,9)
print("Position of repeated element is ",k)
