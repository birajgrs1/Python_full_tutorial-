class Salary:
    def __init__(self, salary):
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)

class Manager(Employee, Salary):
    def __init__(self, name, employee_id, salary, department):
        Employee.__init__(self, name, employee_id)
        Salary.__init__(self, salary)
        self.department = department

    def display(self):
        super().display()
        super().display_salary()
        print("Department:", self.department)

class Clerk(Employee):
    def __init__(self, name, employee_id, office):
        super().__init__(name, employee_id)
        self.office = office

    def display(self):
        super().display()
        print("Office:", self.office)


name = input("Enter manager's name: ")
employee_id = input("Enter manager's employee ID: ")
salary = float(input("Enter manager's salary: "))
department = input("Enter manager's department: ")

manager = Manager(name, employee_id, salary, department)
manager.display()


name = input("Enter clerk's name: ")
employee_id = input("Enter clerk's employee ID: ")
office = input("Enter clerk's office: ")

clerk = Clerk(name, employee_id, office)
clerk.display()
