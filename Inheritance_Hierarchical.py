class A:
    def m1(self):
        print('M1 method')

class B(A):
    def m2(self):
        print('M2 method')

class C(A):
    def m3(self):
        print('M3 method')


obj1 = B()
obj1.m1()
obj1.m2()

obj2 = C()
obj2.m1()
obj2.m3()