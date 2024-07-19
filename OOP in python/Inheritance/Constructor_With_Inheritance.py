class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def showDetails(self):
        print(f"Id of employee: {self.id} \n Name of the employee: {self.name}")

class Manager(Employee):
    def showDetails1(self):
        print("Hii, I am manager.")


obj=Manager(100,"Ram Dahal")
obj.showDetails()
obj.showDetails1()
