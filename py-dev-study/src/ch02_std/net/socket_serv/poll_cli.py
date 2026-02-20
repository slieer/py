#!/usr/bin/env python
import socket

port=10000
s=socket.socket()
host=socket.gethostname()
s.connect((host,port))
s.send("hello from the client")
s.close()