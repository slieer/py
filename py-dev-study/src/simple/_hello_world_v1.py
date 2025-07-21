# -*- coding: utf-8 -*-
'''
Created on 2012-9-15
@author: me
'''

def simple():
    print('Hello world version 1.0')
    # %(xx,xx) 是字符串格式化操作符
    print('世界，你好！ %s' %('zhai'))
    #打印回车符
    print("abc\n", "xyz\n", "lmn\n")
    print('name is %s ,sex is %s' %('zhai', 'man'))
    
    #字符串变量赋值``
    username = 'slieer'
    domain = "www.google.com"
    print('username %s ,domain %s' %(username, domain))
    # 字典类型赋值， 等同于： my_map = dict(name = "zhai", age = 30)。
    getTokenInfo = {'status' : 1}
    print('getTokenInfo.status: %s' %(getTokenInfo['status']))

#类定义
class Basic:
    '''定义单个参数方法'''
    def printProperties(self):
        print('no=%s,ver=%s' %(self.no, self.ver))

    def getProperties(self):
        return self.no, self.ver
    '''定义构造函数，并设置默认属性值'''
    def __init__(self, no='default-no', ver='var'):
        self.no = no
        self.ver = ver

# 定义main方法
if __name__ == '__main__' :
    # 调用simple函数
    simple()
    
    #创建Basic类的实例, 使用默认参数值
    c = Basic()
    c.printProperties()
    # 调用有返回值的方法，并做新变量赋值。 使用下划线_占位忽略不需要的值
    x, y = c.getProperties()
    #创建Basic类的实例
    b = Basic(1, 'ssss')
    b.printProperties()
    # 只给一个参数赋值
    c = Basic(1.5)
    c.printProperties()
    # 使用元组参数
    param = ('no-2', 'ver-2')
    d = Basic(*param)
    d.printProperties()
    # 使用字典参数
    param = {'no': 'no-3', 'ver': 'ver-3'}
    e = Basic(**param)
    e.printProperties()
    # 使用参数名称赋值
    f = Basic(no='no-4', ver='ver-4')
    f.printProperties()



