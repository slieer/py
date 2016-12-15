# -*- coding: utf-8 -*-
'''
Created on 2010-7-10
@author: me

Python提供一个标准的模块，称为pickle。使用它你可以在一个文件中储存任何Python对象，之后你又可以把它完整无缺地取出来。这被称为 持久地 储存对象。

还有另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。你可以使用它们中的任一个，而我们在这里将使用cPickle模块。记住，我们把这两个模块都简称为pickle模块。

'''


import cPickle as p
#import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist # remove the shoplist

# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist 
