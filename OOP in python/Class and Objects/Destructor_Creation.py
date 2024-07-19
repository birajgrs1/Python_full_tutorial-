
class Car:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname,self.year)

#     Destructor Creation
    def __del__(self):
        print(f"The car {self.modelname} is being destroyed.")

#     Creating an instance
c1=Car("BMW",2019)
c1.display()

# Deleting the instance will invoke the destructor
del c1