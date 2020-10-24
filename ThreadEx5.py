from threading import *
print(current_thread().getName())
print('Number of threads', active_count())
current_thread().setName('TestThread')
print(current_thread().getName())
print(current_thread().name)