'''
Created on Jul 22, 2015

@author: dev
'''
import unittest
from __builtin__ import reduce


def _1st():
    f = lambda x, y, z : x + y + z
    return f

def f(x): 
    return x % 2 != 0 and x % 3 != 0

def add(x,y): return x + y

def filter_test():
    return filter(f, range(2, 25))
 
def reduce_test():
    return reduce(add, range(3, 10, 2))

def map_test():
    return map(f, range(1, 10)) 

class Test(unittest.TestCase):
    def testName(self):
        print _1st()(1,2,3)
        print _1st()(6, 7, 8)
    
    def testFilter(self):
        print filter_test()
        
    def testReduce(self):
        print reduce_test()
        
    def testMap(self):
        print map_test()
        
        print map(add, range(8), range(8)) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()