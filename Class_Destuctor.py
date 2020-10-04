class Test:
    def __init__(self):
        print('Constructor is called')

    def __del__(self):
        print('Destructor logic is executed')


t = Test()
del t
# t = None
