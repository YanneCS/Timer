#!/usr/bin/env python

import threading
import time

def timer(timerName, delay):
    for x in range(1,11):
        time.sleep(delay)
        print("%s  %s:%s:%s"%(timerName,
                          time.localtime().tm_hour,
                          time.localtime().tm_min,
                          time.localtime().tm_sec))
    print(timerName + " is done!")
    
try:
    myThread1 = threading.Thread(target = timer,
                                name = "Timer 1",
                                args = ("Timer 1", 5))
    myThread2 = threading.Thread(target = timer,
                                name = "Timer 2",
                                args = ("Timer 2", 2))
    myThread1.start()
    myThread2.start()
    myThread1.join()
    myThread2.join()
except:
    print("ERROR")

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
