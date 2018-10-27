#!/usr/bin/env python

import sys
import threading
import time

def timer(timerName, delay, event):
    for x in range(1,11):
        event.wait(delay)
        if not event.is_set():
            time.sleep(delay)
            print("%s  %s:%s:%s"%(timerName,
                              time.localtime().tm_hour,
                              time.localtime().tm_min,
                              time.localtime().tm_sec))
        else: 
            print(timerName + " is done!")
            print("Main thread received a signal.  Time to abort!")
            return   
    print(timerName + " is done!")

event = threading.Event()
myThread1 = threading.Thread(target = timer,
                                name = "Timer 1",
                                args = ("Timer 1", 5, event))
myThread2 = threading.Thread(target = timer,
                                name = "Timer 2",
                                args = ("Timer 2", 2, event))
myThread1.start()
myThread2.start()
try:
    myThread1.join()
    myThread2.join()
except KeyboardInterrupt as e:
    print("Caught the keyboard break! " + str(e))
    event.set()
    myThread1.join()
    myThread2.join()
    sys.exit()
    
print("I'm finished!")
while 1:
    pass

'''
for x in range(1,11):
    #if((time.localtime().tm_sec %5) == 0):
    
    print("Timer 1 %s:%s:%s"%(time.localtime().tm_hour,
                              time.localtime().tm_min,
                              time.localtime().tm_sec))
    print("Timer 2 %s:%s:%s"%(time.localtime().tm_hour,
                              time.localtime().tm_min,
                              time.localtime().tm_sec))
    time.sleep(2)
'''
