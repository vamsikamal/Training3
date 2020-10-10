class A:
    def m1(self):
        print('M1 method')

class B(A):
    def m2(self):
        print('M2 method')

class C(B):
    def m3(self):
        print('M3 method')


obj = C()
obj.m1()
obj.m2()
obj.m3()