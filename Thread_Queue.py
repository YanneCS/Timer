#!/usr/bin/env python
import Queue
import threading
import time
import random

class myThread (threading.Thread):
    def __init__(self, name, delay, q):

        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.q = q
    def run(self):
        print(self.name + " has started with a delay of " + str(self.delay) + ".\n")
        timer(self.name, self.delay, self.q)
        print(self.name + " is done!")
        
def timer(timerName, delay, q):
    for x in range(1,11):
        time.sleep(delay)
        print("%s  %s:%s:%s\n"%(timerName,
                          time.localtime().tm_hour,
                          time.localtime().tm_min,
                          time.localtime().tm_sec))
    queueLock.acquire()
    if not q.empty():
        q.get()
    queueLock.release()
        
threadList = []
queueLock = threading.Lock()
workQueue = Queue.Queue(4)

        
try:
    for x in ["Timer 1", "Timer 2", "Timer 3", "Timer 4"]:
        print(x)
        threadList.append(myThread(x, random.randint(1,5), workQueue))
    queueLock.acquire()
    for thread in threadList:
        workQueue.put(thread)
    queueLock.release()
    for y in threadList:
        y.start()
    for z in threadList:
        z.join()
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
