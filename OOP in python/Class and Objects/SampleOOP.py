class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)

emp1 = Employee("Biraj", 22)
emp2 = Employee("Ravi", 23)

emp1.display()
emp2.display()  
