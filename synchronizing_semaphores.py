import threading
import time

# Semaphores are used to limit the number of threads that can access
# a certain resoure at a time

# In this case we defined the max number of threads to be 5
semaphore = threading.BoundedSemaphore(value=5)

def access(number):
    print('{} is trying to access'.format(number))
    semaphore.acquire()
    print('{} was able to access'.format(number))
    time.sleep(10)
    print('{} is releasing'.format(number))
    semaphore.release()

for n in range(10):
    threading.Thread(target=access, args=(n,)).start()
    time.sleep(1)
