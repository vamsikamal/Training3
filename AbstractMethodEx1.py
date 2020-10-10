from abc import *
class Test():
    @abstractmethod
    def m1(self):
        pass

    #def m2(self):
     #   print('Hello')


t = Test()
t.m1()
#t.m2()