
class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

obj=Rectangle(2,4)
print("Area of Rectangle: ",obj.area())