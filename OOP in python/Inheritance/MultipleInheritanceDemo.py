
class ParentClass1:
    def func1(self):
        print("I am parent1.")

class ParentClass2:
    def func2(self):
        print("I am parent2.")

class ChildClass(ParentClass1, ParentClass2):   #Multiple Inheritance
    def func3(self):
        print(" I am Child.")

obj=ChildClass()
obj.func1()
obj.func2()
obj.func3()