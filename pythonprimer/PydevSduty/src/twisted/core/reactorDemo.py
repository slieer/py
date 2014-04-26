# -*- coding: utf-8 -*-
'''

反应器按照给定的时间来调用指定的函数。一旦反应器开始运行，反应器就会控制事件循环，并在指定时间调用函数。
反应器在被告知停止之前会一直运行，直到reactor.stop()调用。一旦反应器停止了，程序将继续处理最后一行，
显示反应器停止的消息。
Created on 2011-9-13
@author: slieer
'''
from twisted.internet import reactor
import time

def printTime():
    print 'Current time is', time.strftime("%H:%M:%S")

def stopReactor():
    print "Stopping reactor"
    reactor.stop()

def printSum(i):
    print "sum 1+2+3+...+10= %s" %((1 + i) * i /2)

class result :
    reactor.callLater(1, printTime)   #first second /注册一个1秒后的回调，
    reactor.callLater(2, printTime)   #注册一个2秒后的回调，
    reactor.callLater(3, printTime)
    reactor.callLater(4, printTime)
    
    reactor.callLater(0, printSum, 10)
    
    reactor.callLater(6, stopReactor)
    print 'Running the reactor ...'
    
    reactor.run()
    
    print 'Reactor stopped.'

result()
