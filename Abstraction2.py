from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
    def m2(self):
       print('Hello')

class Child(Test):
    def m1(self):
        print('M1 method')
    def m2(self):
        print('Hi')

t = Child()
#t.m1()
t.m2()