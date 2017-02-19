#!/usr/bin/env python
import socket
import select

'''
Python中的select模块包含了poll()和select(),
select的原型为(rlist,wlist,xlist[,timeout]),
其中rlist是等待读取的对象，
wlist是等待写入的对象，
xlist是等待异常的对象，最后一个是可选对象，指定等待的时间，单位是s.  
select()方法的返回值是准备好的对象的三元组，若在timeout的时间内，没有对象准备好，那么返回值将是空的列表。
'''
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('',10000))

server.listen(5)
inputs=[server]
while 1:
    rs,ws,es=select.select(inputs,[],[],1)
    for r in rs:
        if r is server:
            clientsock,clientaddr=r.accept();
            inputs.append(clientsock);
        else:
            data=r.recv(1024);
            if not data:
                inputs.remove(r);
            else:
                print(data)
                