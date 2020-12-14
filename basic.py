import threading
import time

def counting(x):
    print(time.time())
    for n in range(0, x):
        print('ONE')

def counting2():
    print(time.time())
    for n in range(0, 10):
        print('TWO')


t1 = threading.Thread(target=counting, args=(10,)) # <- Passing arguments. Notice the extra ','
t2 = threading.Thread(target=counting2)


# While this metod is executing on a separate thread the main one keeps going
t1.start()

t2.start()

# You can use the join function to "merge a thred  with the main one"
# This way, the rest of the main code will only execute when the first thread is finished
# > t1.join() <

# This shows the main thread working
print('Hello')