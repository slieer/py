# -*- coding: utf-8 -*-
'''
Created on 2012-9-15
@author: me
'''

def simple():
    print('Hello world version 1.0')
    
    print('世界，你好！')
    print("abc\n", "xyz\n", "lmn\n")
    print('name is %s ,sex is %s' %('zhai', 'man'))
    
    username = 'slieer'
    domain = "www.google.com"
    print('username %s ,domain %s' %(username, domain))

    getTokenInfo = {'status' : 1}
    print('getTokenInfo.status: %s' %(getTokenInfo['status']))


class Basic:
    def printProperties(self):
        print('no=%s,ver=%s' %(self.no, self.ver))
    def __init__(self, no='default-no', ver='var'):
        self.no = no
        self.ver = ver
 
if __name__ == '__main__' :
        simple()
        
        b = Basic(1, 'ssss')
        b.printProperties()
        c = Basic()
        c.printProperties()


