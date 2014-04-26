# -*- coding: utf-8 -*-
'''
Created on 2011-9-11
@author: me

测试：telnet localhost 51423
'''

import socket
host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is runing on port %d; press Ctrl-C to terminate. " \
    %port

while 1 : 
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("Welcome, " + str(clientaddr) + '\n')
    clientfile.write('Please enter a string: ')
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" %len(line))
    clientfile.close()
    clientsock.close()



