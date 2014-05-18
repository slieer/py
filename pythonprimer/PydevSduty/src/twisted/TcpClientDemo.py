# -*- coding: utf-8 -*-
'''
调用reactor.connectTCP()方法打开一个TCP连接，传递一个ClientFactory对象作为第三个参数。
ClientFactory对象等待连接被建立，然后创建一个Protocol对象来管理连接中的数据流。

Created on 2011-9-13
@author: slieer
'''

from twisted.internet import reactor, protocol

class QuickDisconnectedProtocol(protocol.Protocol):
    def connectionMade(self):
        print "Connected to %s." % self.transport.getPeer().host
        self.transport.loseConnection()

class BasicClientFactory(protocol.ClientFactory):
    protocol = QuickDisconnectedProtocol
    def clientConnectionLost(self, connector, reason):
        print 'Lost connection: %s' % reason.getErrorMessage()
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed: %s' % reason.getErrorMessage()
        reactor.stop()

reactor.connectTCP('www.google.com', 80, BasicClientFactory())
reactor.run()
