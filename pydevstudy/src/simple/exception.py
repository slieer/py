# -*- coding: utf-8 -*-

'''
Created on 2010-7-10
我们尝试读取用户的一段输入。按Ctrl-d，看一下会发生什么。
@author: me
'''
import sys

try:
    s = raw_input('Enter something --> ')
except EOFError as e:
    print '\nWhy did you do an EOF on me?'
    print e
    sys.exit() # exit the program
except:
    print '\nSome error/exception occurred.'
    # here, we are not exiting the program

print 'Done' 