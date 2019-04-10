#!/usr/bin/env python

import sys
import threading
import time

def timer(timerName, delay, event):
    for x in range(1,11):
        if not event.is_set():
            print("%s  %s:%s:%s"%(timerName,
                              time.localtime().tm_hour,
                              time.localtime().tm_min,
                              time.localtime().tm_sec))
            time.sleep(delay)
            # event.wait(delay)
        else: 
            print( timerName + " received main thread a signal.  Time to abort!")
            return   
    print(timerName + " is done!")

event = threading.Event()

myThread1 = threading.Thread(target = timer,
                                name = "Timer 1",
                                args = ("Timer 1", 5, event))
myThread2 = threading.Thread(target = timer,
                                name = "Timer 2",
                                args = ("Timer 2", 2, event))
#myThread1.daemon=True
#myThread2.daemon=True




try:
    myThread1.start()
    myThread2.start()
    while myThread1.isAlive():
        myThread1.join(1)
    while myThread2.isAlive():
        myThread2.join(1)
except KeyboardInterrupt as e:
    print("Caught the keyboard break! " + str(e))
    event.set()
    
print("I'm finished!")
