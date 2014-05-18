'''
Created on -9-

@author: root
'''
from twisted.internet import reactor, defer
     
class Getter:
    def getData(self, x):
        # this won't block
        d = defer.Deferred()
        d.addCallback(printData)
        
        reactor.callLater(1, d.callback, x * 3)
        reactor.callLater(3, reactor.stop)
        #return d
    def getData1(self, x):
        # this won't block
        d = defer.Deferred()
        d.addCallback(printData)
        reactor.callLater(0, d.callback, x * 3)
     
def printData(d):
    print 'asyn result: %s' %d

if __name__ == '__main__':
    g = Getter()
    #g.getData(6)
    g.getData1(6)
    reactor.run()
