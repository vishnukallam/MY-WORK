'''ﬁle = open("f.txt", "r")
data =file.readline()
print(data)
file.close()
file = open("f.txt","w")
file.write("Hello World!")'''
class Employee:     
    def __init__(self, name,department, salary):
        self.name = name        
        self.department = department        
        self.salary = salary     
    def read_info(self):
        self.name = input("Enter employee name: ")        
        self.department = input("Enter employee department: ")        
        self.salary = ﬂoat(input("Enter employee salary: "))     
    def print_info(self):
        print("Employee Name:", self.name)        
        print("Department:", self.department)        
        print("Salary:", self.salary)
emp = Employee()
emp.read_info() 
emp.print_info()