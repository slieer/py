#!/usr/bin/env python

import glob
import os

def function(arg1="hello", arg2="slieer"):
    print "arg1:%s" %arg1
    print "arg2:%s" %(arg2)


def foo(*args):
    numArgs = len(args)
    print "Number of arguments:%s" %numArgs
    for i, x in enumerate(args):
        print "Argument %s is %s" %(i,x)
def findFiles():
    files = glob.glob('*.py')
    for x in files:
        real = os.path.realpath(x)
        print real

if __name__ == '__main__':
    function()
    foo('x','y','z')
    findFiles()