'''
Created on 2011-9-13

@author: slieer
'''
from SocketServer import BaseRequestHandler, ThreadingTCPServer
from time import sleep
import sys, socket

class WebLogHandler(BaseRequestHandler):
    def handle(self):
        print"Connected from", self.client_address
        self.request.sendall('<hits>')
        try:
            while True:
                for hit in LOG.readlines():
                    self.request.sendall(hit)
                sleep(5)
        except socket.error:
            self.request.close()
        print"Disconnected from", self.client_address
if __name__=='__main__':
    global LOG
    LOG = open('access-log')
    LOG.seek(0, 2)     # Start at end of current access log
    srv = ThreadingTCPServer(('',8888), WebLogHandler)
    srv.serve_forever()
