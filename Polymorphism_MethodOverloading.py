class Test:
    def m1(self):
        print('M1 is called')

    def m1(self, a):
        print(a)

    def m1(self, a, b):
        print(a+b)


obj = Test()
obj.m1()   # will not work
obj.m1(10) # will not work
obj.m1(10, 20)  # latest method will only work
