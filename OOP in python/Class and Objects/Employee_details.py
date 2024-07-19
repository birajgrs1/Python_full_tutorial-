class Employee:
    def set_EmployeeData(self, id, name, addr, phone, email, salary):
        self.empId = id
        self.name = name
        self.address = addr
        self.phone_no = phone
        self.email_id = email
        self.salary = salary

    def get_EmployeeDetails(self):
        print(f"Employee Id: {self.empId}\nEmployee Name: {self.name}\nEmployee's Address: {self.address}\n"
              f"Employee's phone number: {self.phone_no}\nEmail id: {self.email_id}\nSalary: {self.salary}")


emp1 = Employee()
emp1.set_EmployeeData(input("Enter employee id: "),
                      input("Enter Employee's Name: "),
                      input("Enter employee Address: "),
                      input("Enter Employee's phone number: "),
                      input("Enter Email_id: "),
                      input("Enter Salary: "))

print("\n----------------Employee Details ---------------------- ")
emp1.get_EmployeeDetails()
