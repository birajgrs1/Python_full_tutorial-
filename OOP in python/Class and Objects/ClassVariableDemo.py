
class Student:

    # Class Variable
    schoolName='Texas School'
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no


#     Class method
    @classmethod
    def getSchoolName(cls):
        print(f"School Name: {cls.schoolName}")

s1=Student('Ram',16,2)
print(s1.name,s1.age,s1.roll_no,Student.schoolName)  # Access class variable

s2=Student('Sita',14,1)
# Access class variable
print(s2.name,s2.age,s2.roll_no,Student.schoolName)

# Modification of class variable is use reference as class
Student.schoolName='Trinity School'
print(Student.schoolName)
print(s1.schoolName)
print(s2.__dict__,s2.schoolName)

Student.getSchoolName()
