'''
Created on 2012-11-4

@author: me
'''
import unittest

"""
http://docs.python.org/2/tutorial/stdlib2.html
"""
class Test(unittest.TestCase):

    def testWeakref(self):
        import weakref, gc
        a = A(10)                   # create a reference
        d = weakref.WeakValueDictionary()
        d['primary'] = a            # does not create a reference
        d['primary']                # fetch the object if it is still alive
        del a                       # remove the one reference
        gc.collect()                # run garbage collection right away
        #d['primary']  

    def arrayTest(self):
        from array import array
        a = array('H', [4000, 10, 700, 22222])
        print sum(a)
        print a[1:3]

if __name__ == "__main__":
    import sys;
    sys.argv = ['Test.arrayTest']
    unittest.main()
    
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)