#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os

def func_arg_1(arg1="hello", arg2="slieer"):
    print("arg1:%s" %arg1)
    print("arg2:%s" %(arg2))


def fun_arg_2(*args):
    print(str(args))
    numArgs = len(args)
    print("Number of arguments:%s" %numArgs)
    for i, x in enumerate(args):
        print("Argument %s is %s" %(i,x))

def fun_var_args(farg, *args):
    print('args[]:' + str(args))

    print("arg:", farg)
    for value in args:
        print("another arg:", value)

def fun_var_kwargs(farg, **kwargs):
    print('kwargs{}:' + str(kwargs))
    print("arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

def fun_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def findFiles():
    files = glob.glob('*.py')
    for x in files:
        real = os.path.realpath(x)
        print(real)

if __name__ == '__main__':
    func_arg_1()
    func_arg_1(arg1='xx', arg2='xxxx')
    fun_arg_2('x','y','z')

    # *args可以当作可容纳多个变量组成的list
    fun_var_args(1, "two", 3)

    # myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
    fun_var_kwargs(farg=1, myarg2="two", myarg3=3)

    args = ["two", 3] #list
    fun_var_args_call(1, *args)

    findFiles()