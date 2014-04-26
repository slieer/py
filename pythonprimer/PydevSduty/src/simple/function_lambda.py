# -*- coding: utf-8 -*-
'''
Created on 2011-9-27
@author: root
'''

'''
def f(x):
    return x*2
print f(3)
用lambda表达式实现
'''
g = lambda x: x * 2


#该函数没有函数名称 ,忽略了 return 关键字
#lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。

class CRecord :
    def __init__(self):
        self.a = 'hello'
    
    def func(self):
        print self.a;
    def __str__(self):
        aVar = self.a;
        stri = lambda : aVar *2
        return '__str__ print %s' %(stri())


if __name__ == '__main__' :
    print g(3)
    c = CRecord()
    setattr(c,'a','Hello world,zhai')
    print 'c.a=%s' %(c.a)
    
    '''
    c.__str__ = lambda :c.a
    print c
    '''
    print 'getattr %s' %(getattr(c,'a'))
    print c







