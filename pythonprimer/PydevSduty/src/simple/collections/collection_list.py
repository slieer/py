# -*- coding: utf-8 -*-
'''
Created on 2010-7-3
@author: me
#filename: collection_list

list 动态数组, 可以做为队列，堆栈使用
print语句的结尾使用了一个 逗号 来消除每个print语句自动打印的换行符。
'''
class ListTest:
    shoplist = ['apple','mango','carrot','banana']
    
    def get(self):
        ''''get 1, -1'''
        print 'get  element ,index is 1', ListTest.shoplist[1]
        print 'get  element ,index is -1', ListTest.shoplist[-1]
        
        sub = ListTest.shoplist[-1:]       #片段操作符，用于子list的提取
        print 'sub[-1]:' , sub
        
        sub = ListTest.shoplist[0:1]       #片段操作符，用于子list的提取
        print 'sub[1]:' , sub

    def _len(self):
        print 'I have', len(ListTest.shoplist), ' items to purchase.'
        
    def _list(self):
        print 'These items are:',   #Notice the comma at end of the line
        for item in ListTest.shoplist :
            print item,
    def append(self):        
        print '\nI also have to buy rice.'
        ListTest.shoplist.append('rice')
        print 'My shopping list is now', ListTest.shoplist
        
        ListTest.shoplist  = ListTest.shoplist + [1,2]+[3,4]
        print ListTest.shoplist ;

    def append1(self):
        ListTest.shoplist[0:0] = ['sample value']
        print ListTest.shoplist
        
        ListTest.shoplist[0:1] = ['sample value']
        print ListTest.shoplist
    def _del(self):
        del  ListTest.shoplist[0]
        print ListTest.shoplist
        
class StackTest:
    def __init__(self, arrayOjb=[]):     #class StackTest(object): def __new__(self, arrayOjb=[]):   出错？？？？
        print 'init stack test...'
        self.array = arrayOjb
    def enterStack(self, obj):
        self.array.append(obj)
    def readStactTop(self):
        return self.array[len(self.array) -1]
    def popStactTopElement(self):
        return self.array.pop()
        
from collections import deque
class QueueTest:
    def __init__(self, array):
        self.deque = deque(array)
    def read(self):
        deque.popleft()
    def write(self):
        deque.append("Terry")
        deque.append("Graham")
     
def initArr():    
    initList = [];
    for i in range(3, 10):
        initList.append(i)
        
    initList.insert(0, 10)
    print initList

def foo():
    return 3, 5.5
alpha, beta = foo()

if __name__ == "__main__" :
    li = ListTest()
    li.get()
    print ' --------------------------'
    li.append()
    print ' --------------------------'
    li.append1()
    li._del()
    
    s = StackTest(['b','bb'])
    s.enterStack("a")
    s.enterStack('a1' )
    s.enterStack('a11')
    s.enterStack('a2')
    
    print s.readStactTop()
    print s.popStactTopElement()    
 
    
    

