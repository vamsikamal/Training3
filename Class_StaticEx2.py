class Test:
    x = 0
    def __init__(self):
        Test.x = Test.x + 1
        self.y = 20

t1 = Test()
print(t1.x, t1.y)
t2 = Test()
print(t2.x, t2.y)
