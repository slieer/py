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
        print  'this is a private method.'
    def tostr(self):
        print 'a=%s,b=%s' %(self.a,self.b)

if __name__ == '__main__':
    t = Test()
    t.tostr()
    t._privateMethod()
    
    setattr(t,'c', 'cc')
    t.d = 'ddd'
    t.__dict__['e'] = 'eee'
    print 't.c=%s,t.d=%s,t.e=%s' %(t.c, t.d, t.e)
