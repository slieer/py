#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Apr 23, 2015

@author: dev
'''
import socket
localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
print "local ip:%s "%localIP

ipList = socket.gethostbyname_ex(socket.gethostname())[3]
for i in ipList:
    if i != localIP:
        print "external IP:%s"%i 