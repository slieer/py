'''
Typical Python file structure.
Created on 2010-7-17
@author: me
'''

#/usr/bin/env/ python
"this is a test moudle"     #module documentation
import sys   
import os 

debug = True

class FooClass(object):
    "Foo class"
    pass

def test():
    "test function"
    foo = FooClass()
    if debug:
        print "ran test()"
        
if __name__ == '__main__':
    test();
    print "asAAAAa".lower();


