# -*- coding: utf-8 -*-
'''
Created on 2011-9-28

@author: root
'''
ar = [['abc','xyz'],
      ['m','l','n']
     ]

print(ar[0][0])

arr = [['slieer']]

print(arr[0][0])

import types
print(type(ar) is list)
print(isinstance(ar, list))

print(dir(types))

#类型提示。但这只是一种注解，并不能在运行的时候去检查对与错。
def add(x:int,y:int)->int:
    return x+y

print(add(10,12))
print(add('hello','world')) # 无法做到检查

x = 1
y = 2
(y, x) = (x, y)
#print("x=" + x  + ", y=" + y)

# fib.py
from typing import Iterator
 
 
def fib(n: int) -> Iterator[int]:
  a, b = 0, 1
  while a < n:
    yield a
    a, b = b, a + b
 
i = fib(3)
print(next(i))
