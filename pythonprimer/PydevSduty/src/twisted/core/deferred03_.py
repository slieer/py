#-*- coding:utf-8 -*-

'''
Created on 2011-9-
@author: root

telnet localhost 1079
press enter
input hd or sli or j
'''
from twisted.internet import protocol, reactor, defer
from twisted.protocols import basic

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.factory.getUser(user
            ).addErrback(lambda _: "Internal error in server"
            ).addCallback(lambda m:
                          (self.transport.write(m+"\r\n"),
                           self.transport.loseConnection()))
            
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    
    def __init__(self, **kwargs):
        self.users = kwargs
        
    def getUser(self, user):
        return defer.succeed(self.users.get(user, "No such user"))
    
if __name__ == '__main__':
    reactor.listenTCP(1079, FingerFactory(hd='Hello my python world',sli='china',j='plus'))
    reactor.run()