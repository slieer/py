# -*- coding: utf-8 -*-
'''
Created on 2012-10-7
@author: me
'''
#可以导入自己，比如JsonTest
#AttributeError: 'module' object has no attribute 'dumps'
import json

print json.__file__
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)
data_string = json.dumps(data)
print 'JSON:', data_string

names = ['Jane', ['Matt', 'Laura'], 'Julieta', 'John', 'Jack']
test = json.dumps(names)
print(test)
 

