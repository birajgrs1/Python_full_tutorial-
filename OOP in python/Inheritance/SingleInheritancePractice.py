
# Employee management

class Employee:

    def __init__(self,name,empId):
        self.empId=empId
        self.name=name

    def show(self):
        print("Employee's Id: ", self.empId)
        print("Employee's Name: ", self.name)

class Manager(Employee):
    def __init__(self,empId,name,department):
        super().__init__(name, empId)
        self.department = department

    def show(self):
        super().show()
        print("Department: ", self.department)

empId=input("Enter Employee Id:")
name=input("Enter Employee Name:")
department=input("Enter Department:")

print("\n-------------------------------------\n")
manager=Manager(empId,name,department)
manager.show()

