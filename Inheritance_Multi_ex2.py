class Person:
    def __init__(self):
        print('Person class constructor executed')

    def display(self):
        print('Person class display method called')

class Person2:
    def __init__(self):
        print('Person2 class constructor executed')

    def display(self):
        print('Person2 class display method called')

    def wish(self):
        print('Wish method is called')

class Student(Person, Person2):
    def __init__(self):
        super().__init__()
        print('Student class constructor executed')

    def display(self):
        super().display()
        super().wish()
        print('Student class display method called ')



s = Student()
s.display()