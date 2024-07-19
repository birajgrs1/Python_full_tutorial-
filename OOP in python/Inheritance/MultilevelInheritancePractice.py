class Employee:
    def __init__(self, name, empId):
        self.empId = empId
        self.name = name

    def show(self):
        print("Employee's Id:", self.empId)
        print("Employee's Name:", self.name)


class Manager(Employee):
    def __init__(self, name, empId, department):
        super().__init__(name, empId)
        self.department = department

    def show(self):
        super().show()
        print("Department:", self.department)


class SeniorManager(Manager):
    def __init__(self, name, empId, department, level):
        super().__init__(name, empId, department)
        self.level = level

    def show(self):
        super().show()
        print("Level:", self.level)


empId = input("Enter Employee Id: ")
name = input("Enter Employee Name: ")
department = input("Enter Department: ")
level = input("Enter level: ")

print("\n-------------------------------------\n")

senior_manager = SeniorManager(name, empId, department, level)
senior_manager.show()
