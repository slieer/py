# -*- coding: utf-8 -*-
'''
Created on May 14, 2014
https://docs.python.org/2/faq/programming.html
@author: root
'''
import unittest

def foo(bar=[]):
    bar.append("baz")
    return bar

def fooModified(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

def classTest():
    class A(object):
        x = 1
    class B(A):
        pass
    class C(A):
        pass
    
    B.x = 2
    print(A.x, B.x, C.x)
    
    """在Python中，类变量在内部当做字典来处理，其遵循常被引用的方法解析顺序（MRO）。
    所以在上面的代码中，由于class C中的x属性没有找到，它会向上找它的基类（尽管Python支持多重继承，但上面的例子中只有A）。
    换句话说，class C中没有它自己的x属性，其独立于A。因此，C.x事实上是A.x的引用。"""
    A.x =3
    print(A.x, B.x, C.x)

"""
Python 2和Python 3都支持这种异常语法
"""
def exceptionTest():
    try:
        l = ["a", "b"]
        int(l[2])
    except (ValueError, IndexError) as e:
        pass

x = 10    
def scope():
    global x
    print(x)
    x += 1
    print(x)
    

class Test(unittest.TestCase):

    def testParam(self):
        print(foo())
        print(foo())
        
        arr = ["aa"]
        print("Have a Param:", foo(arr))
        arr1 = ["bb"]
        print(foo(arr1))
        
    def testParam1(self):
        print(fooModified())
        print(fooModified())
        
    def testClass(self):
        classTest()

    def testExce(self):
        exceptionTest()
        
    def testScope(self):
        scope()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()