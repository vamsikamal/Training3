class Test:
    x = 10       # Public
    _y = 20      # Protected
    __z = 30     # Private

    def display(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

    def __wish(self):
        print('Wish')

t = Test()
t.display()
t.__wish()            # Can't be accessible because it is private
print(Test.x)
print(Test._y)
print(Test.__z)       # Can't be accessible because it is private