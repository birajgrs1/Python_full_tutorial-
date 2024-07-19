
from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def abstractFunc(self):   #is supposed to have different implementation in child classes
        pass
    def demoFunc(self):
        print("Inside a demo method of parent class")

class Child1(Parent):
    def abstractFunc(self):   #Concrete methods
        print('Inside the abstract method of Child1')

class Child2(Parent):
    def abstractFunc(self):   #Concrete methods
        print('Inside the abstract method of Child2')


obj1= Child1()
obj1.demoFunc()
obj1.abstractFunc()

obj2= Child2()
obj2.demoFunc()
obj2.abstractFunc()


