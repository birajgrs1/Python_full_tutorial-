
class Employee:
    def __init__(self, id,name):
        self.id=id
        self.name=name


class Manager(Employee):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary

    def showDetails(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")

obj=Manager(1,'Ram Dahal',50000)
obj.showDetails()
