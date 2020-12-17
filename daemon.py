import threading
import time

# Daemon threads as closes as soon as the main thread is closed.
# In other words, the main threads doesn't wait for the Daemon thread to finish.

text = ""

def readFile():
    global text
    while True:
        with open('text.txt', "r") as f:
            text = f.read()
        time.sleep(3)

def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


threading.Thread(target=readFile, daemon=True).start()
printLoop()
