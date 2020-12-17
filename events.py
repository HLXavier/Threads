import threading

# Event is an object that contains a boolean variable (event.isSet()).
# envent.wait() is waiting for the event to be triggered(varible becoming true)
event = threading.Event() 

# We can optionally set a limit of time for the wait function, so we won't be running the
# program forever if the users aswere is "no" (time out)
def func():
    print("Waiting for event")
    event.wait(3)
    if(event.isSet()):
        print("Now we go!")
    else:
        print("Program timed out")

threading.Thread(target=func).start()

user = input("Are you ready? [y/n] ")
if user == "y":
    event.set()

