class Test:
    '''This is a test class for training purpose'''
    def m1(self):
        print('This is test method')


print(Test.__doc__)

obj = Test()
obj.m1()