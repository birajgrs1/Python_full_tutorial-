
class ParentClass:
    def func1(self):
        print('I am parent.')


class Child1(ParentClass):
    def func2(self):
        print('I am child 1.')


class Child2(ParentClass):
    def func3(self):
        print('I am child 2.')


class GrandChild(Child1, Child2):
    def func4(self):
        print('I am grandchild.')


obj = GrandChild()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
