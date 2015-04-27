# -*- coding: utf-8 -*-

'''
last modified 2012-9-29
@author: slieer
'''
class Person:
    i = 10
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name


def f1(self,x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

#空类
class Employee:
    pass

if __name__ == '__main__':
    p = Person('Swaroop')
    p.sayHi()
    print Person.i
    
    x = C()
    print x.f(3,4)
    print x.h() 
    #print C.f()  error.
    print id(x)
    
    john = Employee()
    
    '''动态添加Field''' 
    john.name = 'John Doe'
    john.dept = 'computer lab'
    john.salary = 1000
    
    print john
