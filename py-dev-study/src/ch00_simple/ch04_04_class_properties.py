'''
Created on 2012-9-29

@author: slieer
'''
class Test:
    class_attr = 'slieer'
    def __init__(self,a='defaultA',b='defaultB'):
        self.a = a
        self.b =b
    def _privateMethod(self):
        print('this is a private method.')
    def tostr(self):
        print('a=%s,b=%s' %(self.a,self.b))

class Bar:
    def __init__(self):
         # Leading underscore is convention for "you break it, you bought it"
        self._foo = 3
    
    @property
    def foo(self):
        return self._foo
    

class Rectangle:
    def __init__(self):
        # Leading underscore is convention for "you break it, you bought it"
        self._foo = 3

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, foo):
        if foo % 2 == 0:
            raise ValueError("foo must be odd")
        self._foo = foo

if __name__ == '__main__':
    t = Test()
    t.tostr()
    t._privateMethod()
    
    setattr(t,'c', 'cc')
    t.d = 'ddd'
    t.__dict__['e'] = 'eee'
    print('t.c=%s,t.d=%s,t.e=%s' %(t.c, t.d, t.e))
    
    bar = Bar()
    """AttributeError: can't set attribute
    bar.foo = 0
    """
    print(bar.foo)
    
    
    rect = Rectangle()
    rect._foo = 10
    print(rect.foo)
    
    
    
