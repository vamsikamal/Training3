# Static varibale is common variable for all the objects

class Student:
    org = 'slc'

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    @staticmethod
    def m1():
        print(Student.org)

    def m2(self):
        print(Student.org)

    @classmethod
    def m3(cls):
        print(cls.org)
        print(Student.org)


s1 = Student('Ram', 22, 'Python')
s2 = Student('Raja', 24, 'Java')
print(Student.org)
