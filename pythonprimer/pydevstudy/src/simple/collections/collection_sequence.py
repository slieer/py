# -*- coding: utf-8 -*-
'''
Created on 2010-7-3
序列：python中最基本的数据结构，每一个元素被分配一个需要——元素的位置，亦称“索引”，首个索引为0，第二个为1，后面依此类推。
python包含六种内建的序列类型：列表、元组、字符串、Unicode字符串、buffer对象和xrange对象。
列表、元组和字符串是典型的序列类型，其中，列表可变（可以进行修改），元组和字符串不可变（一旦创建了就是固定的）。

序列的两个主要特点是索引操作符和切片操作符。
序列的神奇之处在于你可以用相同的方法访问元组、列表和字符串。
@author: me
'''
shoplist = ['apple', 'mango', 'carrot', 'banana']

# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1] #倒数第一个
print 'Item -2 is', shoplist[-2] #倒数第二个

# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]  #取下标为1，下标2的两个元素。开始下标为0。
print 'Item 2 to end is', shoplist[2:] #取下标为2,到结尾的所有元素。
print 'Item 1 to -1 is', shoplist[1:-1] #取从下标为1的元素，及后面元素，不含最后一个。就是取除去序列两端的所有元素。
print 'Item start to end is', shoplist[:] #所有元素

# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]   
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:] 


atuple = (2,3,'老子');
alist = list(atuple);
alist[0] = 0
btuple = tuple(alist)

# 去掉重复内容，所以是 1,2,3,4,6
aset = set([1, 2, 3, 2, 4, 6]) 
#建立一个集合的方式，是使用set()函数，函数的参数可以是列表，或者元祖，反正是一串儿的都可以
#集合也是可以变成列表的，利用 list() 函数。
blist = list(aset) 



