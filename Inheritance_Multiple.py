class A:
    def m1(self):
        print('Class A - M1 method call')

class B:
    def m2(self):
        print('Class B - M2 method call')

class C(A, B):
    def m3(self):
        print('M3 is called')


print(C.mro())  # Method resolution order

obj = C()
obj.m1()
# obj.m2()
#obj.m3()
