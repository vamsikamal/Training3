from threading import *
l = RLock()
print('Main thread is locking')
l.acquire()
print('Main thread is locking again ')
l.acquire()
print('Releasing')
l.release()