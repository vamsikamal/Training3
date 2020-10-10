class TooYoungException(Exception):
    def __init__(self):
        self.msg = 'You are too young for this position'


age = int(input('Enter your age: '))
if age < 20:
    raise TooYoungException()
else:
    print('Application accepted')