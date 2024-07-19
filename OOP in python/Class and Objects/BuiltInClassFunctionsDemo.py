
class Student:
    '''This is an example for built in class functions and attributes. '''
    def __init__(self,name,age):
        self.name=name
        self.age=age


s1=Student('Ram',15)
s2=Student('Sita',13)
s3=Student('Jaya',20)


print(getattr(s1,'age'))

setattr(s2,'name','Shyam')
print(s2.__dict__)

print("Before Editing: ",s3.__dict__)
delattr(s3,'age')
print("After Editing: ",s3.__dict__)

# The hasattr()  returns true if an object has the given named attribute and false if it does not.
print(hasattr(s1,'phone_no'))


# Built in attrbutes

print(Student.__doc__)
print(Student.__dict__)
print(Student.__name__)
print(Student.__module__)