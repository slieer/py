# -*- coding: utf-8 -*-
'''
#第一行注释不能少，否则程序中有中文，就会出现文字错误。还有以下写法
Created on 2010-6-26
@author: me
'''
def hello():
    #output Hello world
    print 'Hello world'
    
    #输出  世界，你好！
    print '世界，你好！'
    print "abc\n", "xyz\n", "lmn\n"
    print 'name is %s ,sex is %s' %('zhai', 'man')
    
    username = 'slieer'
    domain = "www.google.com"
    print 'username %s ,domain %s' %(username, domain)
    
    getTokenInfo = {'status' : 1}
    print 'getTokenInfo.status: %s' %(getTokenInfo['status'])
    #print 'getTokenInfo.status: %s' %(getTokenInfo['status1'])  #exception
    
if __name__ == '__main__':
    hello()
