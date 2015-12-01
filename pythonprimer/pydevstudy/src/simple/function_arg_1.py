# -*- coding: utf-8 -*-

#变长参数测试
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


def accept(kwargs):
    for key,value in kwargs.items():
        print "%s ==> %r" %(key,value)

dist1 = {"foo" :'bar',"spam" :'eggs'}
#单个参数，遍 历Map

#多个参数
def accept1(**kwargs):
    for key in kwargs:
        print "%s ==> %r" %(key,kwargs[key])
        

if __name__ == '__main__' :
    print multiply(1,2,3,4,5,6)
    accept(dist1)
    accept1(foo ='bar',spam ='eggs')
    