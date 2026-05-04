# -*- coding: utf-8 -*-
'''
Created on 2011-3-13

@author: me
'''
print('sum output:', sum(i*i for i in range(10)))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]

#zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，
#将对象中对应的元素打包成一个个tuple（元组），
#然后返回由这些tuples组成的list（列表）。
#若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
#利用*号操作符，可以将list unzip（解压），

print('zip output:' , list(zip(xvec, yvec))) #Return a list of tuples,
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product

from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))
print(sine_table)

data = 'golf'
print(list(data[i] for i in range(len(data)-1,-1,-1)))
