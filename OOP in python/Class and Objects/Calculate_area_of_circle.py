
class Circle:

    pi=3.1416    #class variable

    @staticmethod
    def area_of_circle(rad):
        area=Circle.pi*rad*rad
        return area

rad=float(input("Enter radius:"))
print("Area of Circle is ", Circle.area_of_circle(rad))