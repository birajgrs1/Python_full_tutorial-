

class ParentClass:
    def func1(self):
        print('I am parent.')


class ChildClass(ParentClass):
    def func2(self):
        print('I am child.')

obj=ChildClass()
obj.func1()
obj.func2()
