
class Employee:
    def __init__(self, name, empId):
        self.name = name
        self.empId = empId

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.empId)

class Manager(Employee):
    def __init__(self, name, empId, department):
        super().__init__(name, empId)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

class Clerk(Employee):
    def __init__(self, name, empId, office):
        super().__init__(name, empId)
        self.office = office

    def display(self):
        super().display()
        print("Office:", self.office)


name = input("Enter manager's name: ")
empId = input("Enter manager's employee ID: ")
department = input("Enter manager's department: ")

manager = Manager(name, empId, department)
manager.display()


name = input("Enter clerk's name: ")
empId = input("Enter clerk's employee ID: ")
office = input("Enter clerk's office: ")

clerk = Clerk(name, empId, office)
clerk.display()
