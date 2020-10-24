from threading import *
def display():
    print('Child Thread')

t = Thread(target=display)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())
t.start()