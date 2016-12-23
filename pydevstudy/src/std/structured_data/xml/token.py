'''
Created on 2011-9-22
@author: slieer
'''

import socket
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

"""
 get status, msg, uid, msisdn value.
"""
class TokenContentHandler(ContentHandler):
    statusTag = 'status'
    msgTag = 'msg'
    uidTag = 'uid'
    msisdnTag = 'msisdn'
    
    def __init__(self):
        self.status, self.msg, self.uid, self.msisdn = None, None,None, None
        self.tagName = ''
        
    def startElement(self, name, attrs):
        self.tagName = name
    
    def endElement(self, name):
        pass

    def characters(self, chars):
        if self.tagName == TokenContentHandler.statusTag and self.status == None:
            self.status  = chars
        elif self.tagName == TokenContentHandler.msgTag and self.msg == None:
            self.msg = chars
        elif self.tagName == TokenContentHandler.uidTag and  self.uid == None:
            self.uid = chars
        elif self.tagName == TokenContentHandler.msisdnTag and self.msisdn == None:
            self.msisdn = chars
            
def get(file_):
    handler = TokenContentHandler()
    parser = make_parser()
    parser.setContentHandler(handler)
    try:
        parser.parse(file_)
        file_.close()
        return handler.status, handler.msg, handler.uid, handler.msisdn
    except Exception as e:
        print(e)        

def sendRequest(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host,port)
    return s.makefile("rw", 0)

    #for line in fd.readlines():
    #   sys.stdout.write(line)

if __name__ == '__main__':
    host = ""
    port = ""
    file = sendRequest(host, port)
    print(get(file))

