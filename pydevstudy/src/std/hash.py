#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on May 11, 2014

@author: root
'''

import os
import hashlib

src = "teststring"
val = hashlib.md5(src).hexdigest();
print(val)

m0 = hashlib.md5()
m0.update(src)
m0.update('hi')
m0.update('slieer')
val = m0.hexdigest().upper()
print val

"""file test"""
def getFileMd5(fileName):
    if not os.path.isfile(fileName) :
        return
    myHash = hashlib.md5();
    f = file(fileName, 'rb')
    
    while True :
        b = f.read(8096);
        if not b :
            break
        myHash.update(b)
    f.close()
    return myHash.hexdigest().upper()

print getFileMd5('./hash.py')

    