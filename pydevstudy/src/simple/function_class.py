# -*- coding: utf-8 -*-
'''
Created on 2011-9-19
学习使用 getattr 和__call__用法 , 参数默认值
@author: slieer
'''
class A:
    def __init__(self):
        self.a = 'a'
    def method(self):
        print "method print"

#__call__解释： 一个类型定义了__call__方法，那么这个类型的对象可以做为一个函数使用，__call__只能定义一次
class Animal(object):
    def __init__(self, name, legs):        
        self.name = name
        self.legs = legs
        self.stomach = []          
    def __call__(self,food):   
        self.stomach.append(food)
    def poop(self):
        if len(self.stomach) > 0:       
            return self.stomach.pop(0)     
    def __str__(self):                
        return 'A animal named %s' % (self.name)

def getattrTest():    
    a = A()
    print getattr(a, 'a', 'default') #如果有属性a则打印a，否则打印default
    print getattr(a, 'b', 'default') #如果有属性b则打印b，否则打印default
    print getattr(a, 'method', 'default') 
    #如果有方法method，否则打印其地址，否则打印default
    print getattr(a, 'method', 'default')()
    #如果有方法method，运行函数并打印None否则打印default

def callTest():
    cow = Animal('king', 4)
    dog = Animal('flopp', 4)  #We can make many animals
    print 'We have 2 animales a cow name %s and dog named %s,both have %s legs' % (cow.name, dog.name, cow.legs)
    print cow  #here __str__ metod work
    
    #We give food to cowcow('gras')
    print cow.stomach #We give food to dog
    dog('bone')
    dog('beef')
    print dog.stomach #What comes inn most come out
    print cow.poop()
    print cow.stomach  #Empty stomach

class String:
    def _testSplit(self, str,interval):
        return str.split(interval)
    
    def testSplit(self):
        print self._testSplit("slieer@gmail.com", '@')
        
    def testSplit1(self):
        str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
        print str.split();
        print str.split(' ', 1 );   #只分割一次
        
    def __call__(self):
        self.testSplit()
        self.testSplit1()


class DefaultParam:
    def testSimpleDefaultParam(self):
        """默认参数的值在函数定义的时候就被决定,并且不会改变,例如"""
        a = 10
        def foo(x = a):
            print x
        a = 5               # Reassign 'a'.
        foo()               # Prints '10' (默认值没有改变)
        
    def testDefaultParam(self):
        """若使用可变对象作为默认参数值,则会有意料之外的情况发生:""" 
        a = [10]
        def foo(x = a):
            print x
        a.append(20)
        foo()              # Prints '[10, 20]'



""" test code"""        
#运行测试   
#getattrTest()    
#callTest()
#String()()

DefaultParam().testSimpleDefaultParam()
DefaultParam().testDefaultParam()

        







