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

def socketTest():
    '''
    Created on 2011-9-11
    '''
    print("Creating socket...", end=' ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("done")
    
    print("Looking up port number...", end=' ')
    port = socket.getservbyname("http","tcp")
    print("%s done." %port)
    
    print("Connecting to remote host...", end=' ')
    s.connect(('www.google.com',80))
    print("done")
    
    print("Connected form ", s.getsockname())
    print("connected to ", s.getpeername())


def firstExam():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
    except socket.error as e:
        print("Error connecting to server: %s" %e)
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
    secondExam()      
