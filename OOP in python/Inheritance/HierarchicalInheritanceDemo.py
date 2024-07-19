
class ParentClass:
    def func1(self):
        print('I am parent.')


class Child1(ParentClass):
    def func2(self):
        print('I am child 1.')

class Child2(ParentClass):
    def func3(self):
        print('I am child 2.')

obj=Child1()
obj.func1()
obj.func2()

obj2=Child2()
obj2.func1()
obj2.func3()
