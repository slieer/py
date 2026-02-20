# -*- coding: utf-8 -*-
'''
Created on 2012-9-15
@author: me
'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def simple():
    logging.info('Hello world version 1.0')
    # %(xx,xx) 是字符串格式化操作符
    logging.info('世界，你好！ %s' %('zhai'))
    #打印回车符
    logging.info('%s, %s, %s', "abc\n", "xyz\n", "lmn\n")
    logging.info('name is %s ,sex is %s' %('zhai', 'man'))
    
    #字符串变量赋值``
    username = 'slieer'
    domain = "www.google.com"
    print('username %s ,domain %s' %(username, domain))
    # 字典类型赋值， 等同于： my_map = dict(name = "zhai", age = 30)。
    getTokenInfo = {'status' : 1}
    logging.info('getTokenInfo.status: %s' %(getTokenInfo['status']))

#类定义
class Basic:
    '''定义单个参数方法 
       注意：
       每个方法的第一个参数都是self
       self 是Python 中类方法的第一个参数，代表实例对象。 
       self 用于访问和修改实例的属性，以及调用其他实例方法。
    '''
    def printProperties(self):
        logging.info('no=%s,ver=%s' %(self.no, self.ver))

    '''返回一个元组tuple'''
    def getProperties(self):
        return self.no, self.ver
    '''定义构造函数，并设置默认属性值'''
    def __init__(self, no='default-no', ver='var'):
        self.no = no
        self.ver = ver

    """
    str(x) —— 面向用户（User-friendly）
    目标：可读性优先，适合最终用户查看。
    通常返回对象的“简洁”或“自然语言”形式。
    调用对象的 __str__() 方法（如果未定义，则回退到 __repr__()）。
    简单的说，是更加阅读友好的toString

    repr(x) —— 面向开发者（Developer/debugging-friendly）
    目标：准确性与明确性优先，力求“无歧义”。
    理想情况下，eval(repr(x)) == x（即结果可被 eval() 重新构造）。
    调用对象的 __repr__() 方法。
    简单的说是开发人员的toString.
    """
    def __repr__(self):
        pass

    def __str__(self):
        pass

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
    # 使用元组(tuple)参数
    param = ('no-2', 'ver-2')
    d = Basic(*param)
    d.printProperties()
    # 使用字典(dict)参数
    param = {'no': 'no-3', 'ver': 'ver-3'}
    e = Basic(**param)
    e.printProperties()
    # 使用参数名称赋值
    f = Basic(no='no-4', ver='ver-4')
    f.printProperties()

    logging.warning('proprerties: %s', f.getProperties())



