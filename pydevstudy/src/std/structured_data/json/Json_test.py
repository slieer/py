# -*- coding: utf-8 -*-
'''
Created on 2012-10-7
@author: me
'''
#可以导入自己，比如JsonTest
#AttributeError: 'module' object has no attribute 'dumps'
import json

def encoding():
    print json.__file__
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'repr DATA:', repr(data)
    data_string = json.dumps(data)
    print 'JSON:', data_string
    
    names = ['Jane', ['Matt', 'Laura'], 'Julieta', 'John', 'Jack']
    print 'other DATA:', json.dumps(names)

    print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

    print json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))

def deconding():
    obj = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    print 'get Json properties:', obj[0]
    print 'get Json properties:', obj[1]['bar']
    
if __name__ == '__main__':
    encoding()
    deconding()

