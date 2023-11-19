def first_diff(s1,s2):
    if s1 == s2:
        return -1
    else:
        i=0
        while(s1[i]==s2[i]):
            i=i+1
        else:
            print("The first difference occurs at {}".format(i+1))          
s1=input("Enter a string:")
s2=input("Enter a string:")
x=first_diff(s1,s2)
if x==-1:
    print("Strings are equal")
else:
    print("Strings are different") 
