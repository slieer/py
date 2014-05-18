# -*- coding: utf-8 -*-
'''
Created on 2011-9-20
@author: slieer

在命令行
 Download.py www.baidu.com
'''
from twisted.web import client
from twisted.internet import reactor
import sys

def printPage(data):
    print data
    reactor.stop()

def printError(failure):
    print >> sys.stderr, "Error: ",failure.getErrorMessage()
    reactor.stop()
    
if len(sys.argv) == 2 :
    url = sys.argv[1]
    
    #注意：client.getPage(url)，返回了Deferred对象，用于非同步状态下通知下载完成事件。
    client.getPage(url).addCallback(printPage).addErrback(printError)

    #添加回调也可以采用如下方式
    #d=deferredFunction()
    #d.addCallback(resultHandler)
    #d.addCallback(errorHandler)
    
    reactor.run()
else :
    print "Usage: webcat.py <URL>"
