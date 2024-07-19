
class Employee:
    def __init__(self, name, empId):
        self.name = name
        self.empId = empId

    def show(self):
        print("Name:", self.name)
        print("Employee ID:", self.empId)

class Salary:
    def __init__(self, salary):
        self.salary = salary

    def showSalary(self):
        print("Salary:", self.salary)



class Manager(Employee, Salary):
    def __init__(self, name, empId, salary, department):
        Employee.__init__(self, name, empId)
        Salary.__init__(self, salary)
        self.department = department

    def show(self):
        super().show()
        super().showSalary()
        print("Department:", self.department)



empId = input("Enter employee ID: ")
name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")

print("\n---------------------------------\n ")
manager = Manager(empId,name, salary, department)
manager.show()