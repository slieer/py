# -*- coding: utf-8 -*-
'''
Created on 2011-10-9

@author: me
'''
import _thread
import time

#无线程同步
def counter(myId,count):
    for i in range(count) :
        print('[%s] => %s\n' %(myId,i))

#线程同步#
mutex = _thread.allocate_lock()
def syncCounter(myId, count): 
    mutex.acquire()
    for i in range(count):
        print('[%s] => %s\n' % (myId, i))
    mutex.release()

def threadFunc():
    for i in range(5):
        #print "create new thread %s \n"  %(thread.start_new(counter, (i,10)))
        print("create new thread %s \n"  %(_thread.start_new(syncCounter, (i,10))))


        
threadFunc()
time.sleep(1)
print('Main thread existing.')