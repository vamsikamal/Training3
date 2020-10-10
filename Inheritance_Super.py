class Person:
    def __init__(self):
        print('Person class constructor executed')

    def display(self):
        print('Person class display method called')


class Student(Person):
    def __init__(self):
        super().__init__()
        print('Student class constructor executed')

    def display(self):
        super().display()
        print('Student class display method called ')



s = Student()
s.display()