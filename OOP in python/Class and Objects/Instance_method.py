
class Student:
    def __init__(self,name,age):   #Instance variables
        self.name=name
        self.age=age

    def show(self):   #Instance method
        print(f"Name: {self.name} \n Age: {self.age}")

s1=Student('Ram',15)
s1.show()    #Call instance method using object s1

