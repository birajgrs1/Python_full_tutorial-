
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, cname, max_students):
        self.cname = cname
        self.max_students = max_students
        self.students = []
        self.isActive = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        if not self.students:
            return 0  
        total_grade = sum(student.get_grade() for student in self.students)
        return total_grade / len(self.students)

s1 = Student("Ram", 20, 90)
s2 = Student("Shyam", 19, 80)
s3 = Student("Hari", 21, 85)

course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)

print(course.students[0].name)
print(course.get_average_grade())
