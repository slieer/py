# -*- coding: utf-8 -*-
'''
Created on 2010-6-28
全局变量的引用
@author: me
'''
x = 50
def func():
    global x
    print('x is ',x)
    x = 2
    print('Changed local x to ', x)

#注意
def func1(param):
    param = 20
    print("changed local x to ", param)

class Obj(object):
    def __new__(self, a, b):
        self.a = a
        self.b = b
    def toString(self):
        print('a=%s, b=s%s' %(self.a,self.b))
def func2(obj):
    setattr(obj,'a',100)
    
    #obj.b = 120
    
if __name__ == "__main__":
    #传入全局变量
    func()
    #传入值参数
    func1(x)
    print('final x value is ', x)
    
    #传入引用
    o = Obj(1,3)
    func2(o)
    o.toString()
    