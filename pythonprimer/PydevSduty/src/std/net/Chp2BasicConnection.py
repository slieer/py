'''
Created on 2011-9-11
@author: me
'''
import socket
print "Creating socket...",
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done"

print "Looking up port number...",
port = socket.getservbyname("http","tcp")
print "%s done." %port

print "Connecting to remote host...",
s.connect(('www.google.com',80))
print "done"

print "Connected form ", s.getsockname()
print "connected to ", s.getpeername()
