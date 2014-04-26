'''
Created on 2011-9-28

@author: root
'''
from twisted.internet import reactor, threads
import  urllib2
from sys import stdout 

def doLongCalculation():
    # .... do long calculation here ...
    req = urllib2.Request('http://baidu.com')
    response = urllib2.urlopen(req)
    return response

def printResult(response):
    for line in response.readlines():
        stdout.write(line)
    reactor.stop()


# run method in thread and get result as defer.Deferred
d = threads.deferToThread(doLongCalculation)
d.addCallback(printResult)
reactor.run()
