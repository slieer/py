# -*- coding: utf-8 -*-
'''
Created on 2011-9-10
在上一个程序的基础上，加入异常处理，使得异常显示更友好些。
@author: me
'''

import socket,sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

def firstExam():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
    except socket.error, e:
        print "Error connecting to server: %s" %e
        sys.exit()
        
    s.sendall(filename + '\r\n')
    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)


'''
Simple Gopher Client with file-like interface
采用文件的形式操作流
'''      
def secondExam():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host,port)
    fd = s.makefile("rw", 0)
    
    for line in fd.readlines():
        sys.stdout.write(line)
        
if __name__ == '__main__':
    firstExam()        
