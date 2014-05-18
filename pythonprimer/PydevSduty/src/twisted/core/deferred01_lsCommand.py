'''
Created on --
@author: root

telnet localhost 1079
'''
from twisted.internet import protocol, reactor, utils
from twisted.protocols import basic

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.factory.getUser(user
        ).addErrback(lambda _: "Internal error in server"
        ).addCallback(lambda m:
                       (self.transport.write(str(m) + "\r\n"),
                        self.transport.loseConnection()))
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    def getUser(self, user):
        return utils.getProcessOutput("ls", ['-a'])

if __name__ == '__main__':
    reactor.listenTCP(1079, FingerFactory())
    reactor.run()
