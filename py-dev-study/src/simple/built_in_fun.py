'''
Created on Jul 22, 2015

@author: dev
'''
import unittest
from functools import reduce

def f(x): 
    return x % 2 != 0 and x % 3 != 0

# 支持传入一个函数做为参数
def filter_test():
    return list(filter(f, list(range(2, 25))))
 

def add(x, y): return x + y

def reduce_test():
    return reduce(add, list(range(3, 10, 2)))

def map_test():
    return list(map(f, list(range(1, 10)))) 


# 定义一个函数，返回一个lambda表达式
def _1st():
    f = lambda x, y, z : x + y + z
    return f
# 定义一个lambda表达式，直接返回， 等同价于_1st() 
_1st1 = lambda x, y, z : x + y + z

class Test(unittest.TestCase):
    def testName(self):
        # 调用函数的函数
        print(_1st()(1,2,3))
        print(_1st()(6, 7, 8))
        print(_1st1(6, 7, 8))
    
    def testFilter(self):
        print(filter_test())
        
    def testReduce(self):
        print(reduce_test())
        
    def testMap(self):
        print(map_test())
        
        print(list(map(add, list(range(8)), list(range(8))))) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()