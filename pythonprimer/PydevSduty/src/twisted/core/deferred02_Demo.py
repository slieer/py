# -*- coding: utf-8 -*-
'''

当编写一个启动非同步操作的函数时，返回一个Deferred对象。当操作完成时，调用Deferred的callback方法来返回值。
如果操作失败，调用Deferred.errback函数来跑出异常。
例子: 使用Deferred非同步操作的连接，连接一个服务器的端口。

Created on -9-
@author: slieer
'''
from twisted.internet import reactor, defer, protocol
 
class CallbackAndDisconnectProtocol(protocol.Protocol):
    
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")
        self.transport.loseConnection()
        
        
class ConnectionTestFactory(protocol.ClientFactory):
    protocol = CallbackAndDisconnectProtocol
    
    def __init__(self):
        self.deferred = defer.Deferred()   #report deferred event, prevent program block on this task
        
    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)
        
def testConnect(host, port):
    testFactory = ConnectionTestFactory()
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred

def handleSuccess(result, port):
    #deferred "event-responsor": handle finished connection
    print "Connected to port %i" % port
    reactor.stop()
    
def handleFailure(failure, port):
    print "Error connecting to port %i: %s" % (port, failure.getErrorMessage())
    reactor.stop()
    
if __name__ == '__main__':
    import sys
    
    if not len(sys.argv) == 3:
        print "Usage: connectiontest.py host port"
        sys.exit()
        
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    connecting = testConnect(host, port)
    connecting.addCallback(handleSuccess, port)
    connecting.addErrback(handleFailure, port)
    reactor.run()
    