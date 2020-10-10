class Test:
    def __init__(self):
        print('Constructor is called')

    def __init__(self, a):
        print(a)

    def __init__(self, a, b):
        print(a+b)


obj = Test(10, 20)

