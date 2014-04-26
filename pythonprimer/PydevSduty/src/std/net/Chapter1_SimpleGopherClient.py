# -*- coding: utf-8 -*-

"""
这个程序，是可以运行的网络协议实现的最小程序，它实现Gopher协议。
需要两个命令行参数：
    主机名，文件名
实现从主机上请求相关文档的功能

现存的Gogher服务器并不多，所以要测这个例子，还是用以下参数吧：
 在命令行切换到本文件目录下，执行
 Chapter1_SimpleGopherClient.py quux.org /
 
2011-9-10
"""

import socket,sys
port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #IPv4, tcp.
s.connect((host,port))
s.sendall(filename + '\r\n')

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

