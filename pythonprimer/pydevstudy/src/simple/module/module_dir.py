# -*- coding: utf-8 -*-

'''
Created on 2010-7-3
@author: me
sys.modules 打印python模块列表

知道模块名后，如有个str
再dir(str) 可以知道str有哪些方法。

如果想知道方法更细节的方面再来个
或help(str.xxxx)xxxx是str的一个方法名。

'''
import sys
mod = sys.modules

for name in mod.items():
    print name


#get list of attributes for sys module
#print dir(sys)
#help(str)