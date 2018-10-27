#!/usr/bin/env python
import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, delay):

        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print(self.name + " has started.")
        timer(self.name, self.delay)
        print(self.name + " is done!")
        
def timer(timerName, delay):
    for x in range(1,11):
        time.sleep(delay)
        print("%s  %s:%s:%s"%(timerName,
                          time.localtime().tm_hour,
                          time.localtime().tm_min,
                          time.localtime().tm_sec))
        
try:
    myThread1 = myThread("Timer 1", 5)
    myThread2 = myThread("Timer 2", 2)
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
