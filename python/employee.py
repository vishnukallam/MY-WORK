class employee:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def display(self):
        print(f"The name of the employee {self.name} \nDepartment {self.dept} \nSalary {self.salary}")
n,d,s="vishnu","CSE",20000
Emp=employee(n,d,s)
Emp.display()
