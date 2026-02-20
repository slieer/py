# -*- coding: utf-8 -*-
'''
Created on 2011-9-15
@author: slieer
'''
import sys
sys.path.append('/opt/workspace/py/py-dev-study/src')
#导入类
from ch01_module.thinking.in_.python.Test import HelloWorld as Hello

#导入方法
from ch01_module.thinking.in_.python.Test import hello as helloMethod

#导入变量
from ch01_module.thinking.in_.python.Test import abc as abcVirable

print('--------------------------')
h = Hello()
print(h.hello())

print('-----------------------------')
print(helloMethod())

print('-----------------------------')
print(abcVirable)


from ch01_module.thinking.in_.python.ClassFunction import make_adder_as_bound_method as m
m