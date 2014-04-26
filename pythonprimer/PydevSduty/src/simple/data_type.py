# -*- coding: utf-8 -*-
'''
Created on 2011-9-28

@author: root
'''
ar = [['abc','xyz'],
      ['m','l','n']
     ]

print ar[0][0]

arr = [['slieer']]

print arr[0][0]

import types
print type(ar) is types.ListType
print isinstance(ar, list)

print dir(types)