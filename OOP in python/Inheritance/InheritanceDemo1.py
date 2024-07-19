class Parent:
    def func1(self):
        print("I am   parent...")

class Child(Parent):
    def func2(self):
        print("I am child...")

obj=Child()
obj.func1()
obj.func2()