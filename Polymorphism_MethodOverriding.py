class Parent:
    def m1(self):
        print('Parent class m1 method')

class Child(Parent):
    def m1(self):
        print('Child class m1 method')

p = Child()
p.m1()