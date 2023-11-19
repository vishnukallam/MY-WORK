'''def sum_digits(num):
   num = int(input("enter any number"))
   while num !=0:
      sum= 0 
      sum+=num
   return sum
print('the sum of given number is ',sum_digits(sum))'''
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = int(input("enter any number"))
print(getSum(n))