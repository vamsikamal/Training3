class Test:
    def __init__(self, n1, n2):
        # Constructor
        self.a = n1
        self.b = n2
        print('Constructor called')

    def m1(self, m1):
        self.c = m1

    def m2(self):
        print(self.d)

t = Test(10, 20)
print(t.a)
print(t.b)
t.m1(100)
print(t.c)

t.d = 200
t.m2()
print('End of the program')



