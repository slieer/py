'''
Created on 2010-7-3

@author: me
'''
if __name__ == '__nain__' :
    print "This program is being run by itself"
else:
    print 'I an being imported from another module'
    
'''
$ python using_name.py
This program is being run by itself

$ python
>>> import using_name
I am being imported from another module
>>>
'''

'''
每个Python模块都有它的__name__，如果它是'__main__'，
这说明这个模块被用户单独运行，我们可以进行相应的恰当操作。
'''  