'''
Created on 2010-7-11
@author: me
'''

#当有__all___ 时，在其它文件中写from foo import * ，只导入本文件__all__所定义的
#如果在__all__以上注释掉，此代码，然后执行完成，为import *默认的行为是导入所有的符号不以下划线开始从给定的空间。  
__all__ = ['make_adder_as_bound_method',
           'make_adder_as_closure']

def make_adder_as_closure(augend):
    def add(addend, _augend=augend): return addend+_augend
    return add

#Bound methods and callable instances are richer and more flexible than closures. Here's how to implement the same functionality with a bound method:
def make_adder_as_bound_method(augend):
    class Adder(object):
        def __init__(self, augend): self.augend = augend
        def add(self, addend): return addend+self.augend
    return Adder(augend).add

#Here's how to implement it with a callable instance (an instance whose class supplies special method _ _call_ _):
def make_adder_as_callable_instance(augend):
    class Adder(object):
        def __init__(self, augend): self.augend = augend
        def __call__(self, addend): return addend+self.augend
    return Adder(augend)

print make_adder_as_closure(122)
