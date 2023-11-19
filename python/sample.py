class student:
    def __init__(self, age, name) -> int:
        self.age = age
        self.name = name

    def show(self):
        return self.age, self.name


clas = student(12, "revi")
print(clas.show())
print(type(clas))
print(id(clas))
print(id(student))
