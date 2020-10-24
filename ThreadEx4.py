from threading import *
from time import *

def double(numbers):
    for i in numbers:
        sleep(2)
        print('Double the number {0} is {1}'.format(i, i * 2))

def square(numbers):
    for i in numbers:
        sleep(2)
        print('Square of number {0} is {1}'.format(i, i * i))

numbers = [1,2,3,4,5,6,7,8,9,10]
begin = time()
t1 = Thread(target=double, args=(numbers, ))
t2 = Thread(target=square, args = (numbers, ))
t1.start()
t2.start()

t1.join()
t2.join()
end = time()
print('Time taken is: ', end-begin)