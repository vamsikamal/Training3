class A:
    def m1(self):
        print('M1 Method')

class B(A):
    def m2(self):
        print('M2 Method')

obj = B()
obj.m1()
obj.m2()

