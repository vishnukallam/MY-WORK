# # Input numbers as a string
# input_numbers = input("Enter numbers separated by spaces: ")

# # Split the input string into a list of numbers
# numbers = input_numbers.split()
# print(numbers)
# total = 0

# # Initialize a variable to store the equation with plus symbols
# equation = ""

# # Iterate through the list of numbers
# for num in numbers:
#     # Check if the string represents a valid number
#     if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
#         # Convert the string to an integer and add it to the total
#         total += int(num)
        
#         # Add the number to the equation string with a plus symbol
#         equation += num + " + "
#     else:
#         print(f"'{num}' is not a valid number. Skipping.")

# # Remove the trailing ' + ' from the equation
# equation = equation.rstrip(' + ')

# # Display the equation and the total
# print(f"Equation: {equation}")
# print(f"Total: {total}")
# num = int(input())
# fact=1
# #print(factorial(num))
# for i in range(1,num+1):

#     fact = fact*i
# print(fact)
n = int(input("enter a number:"))
d = int(input("enter a number:"))
b = int(bin(n))
l=[]
for i in range(1,b+1):
    l.append(b.strip("0b")) 
print(l)
a = l[-2]
print(l.remove(a))
str()