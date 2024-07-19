
class Car:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname,self.year)

c1=Car("BMW",2019)
c1.display()