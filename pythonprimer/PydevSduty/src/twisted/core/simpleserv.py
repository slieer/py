
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

def main():
    """This runs the protocol on port 8000"""
    reactor.listenTCP(1234, EchoFactory())
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
