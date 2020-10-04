class Outer:
    def __init__(self):
        print('Outer class object created')

    class inner:
        def __init__(self):
            print('Outer class object created ')
        def m1(self):
            print('Inner class method is called')

obj = Outer()
obj2 = obj.inner()
obj2.m1()
