import threading
import time

x = 64.0

# A lock can be acquared by only one thread at a time
# Once it's released, other threads can execute
lock = threading.Lock()

# This effects only the threads that need to acquire the lock

def double():
    global x, lock
    lock.acquire()
    while x < 2048:
        print(x)
        x *= 2
        time.sleep(1)
    print('High number reached')
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        print(x)
        x /= 2
        time.sleep(1)
    print('Low number reached')
    lock.release()

threading.Thread(target=half).start()
threading.Thread(target=double).start()

# In my exemple, the main thread doesn't need to acquire the lock
# Therefore, this text will be printed immediatly after the half thread call
print('Main thread')


