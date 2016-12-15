# -*- coding: utf-8 -*-
'''
Created on 2010-7-4
last modified 2012-9-29
@author: slieer
'''
class Person:
    classVar = 'test class variable.'
    @staticmethod
    def staticMehtod():
        print 'static method called'
        
    def __init__(self):
        print 'call init method...'
    def sayHi(self):
        print 'Hello, how are you?'
        

class Child (Person):
    def canntWalk(self):
        print 'yes, con\'nt walk'

class Pers(object):
    def __new__(self):
        print 'execute new method.'

if __name__ == '__main__':
    p = Person()   #__init__方法被调用
    p.sayHi()
    
    Person.staticMehtod() #类方法，应通过类型调用。
    #p.staticMehtod()   #类方法，也可以通过对象名调用
    print Person.classVar
    print '--------------------------------------'
       
    c = Child()
    Child.staticMehtod(); #类方法也可以被继承
    c.canntWalk()
    print c
    
    print '--------------------------------------'
    Pers() #__new__方法被调用, only call when classes inheriting from object.
