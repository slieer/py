#!/usr/bin/env python
import socket

host='127.0.0.1';
port=10000;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send('hello from client')
s.close();