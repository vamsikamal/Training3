from threading import *
import time

def display():
    print(current_thread().name, 'Started ...')
    time.sleep(3)
    print(current_thread().name, 'Ended ...')

t1 = Thread(target=display, name = 'Thread 1')
t2 = Thread(target=display, name = 'Thread 2')
t3 = Thread(target=display, name = 'Thread 3')
t4 = Thread(target=display, name = 'Thread 4')
t1.start()
t2.start()
t3.start()
t4.start()
enm = enumerate()
for t in enm:
    print ('Thread name is: ', t.name)
    
