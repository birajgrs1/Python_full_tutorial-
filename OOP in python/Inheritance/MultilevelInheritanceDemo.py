
class GrandFather:
    def func1(self):
        print("I am Grandfather.")

class Father(GrandFather):
    def func2(self):
        print("I am Father.")

class GrandSon(Father):
    def func3(self):
        print(" I am Grandson.")

obj=GrandSon()
obj.func1()
obj.func2()
obj.func3()