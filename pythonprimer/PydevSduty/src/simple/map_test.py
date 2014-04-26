'''
Created on Apr 17, 2014

@author: root
'''

def simple():
    def add100(x):
        return x + 100

    hh = [11, 22, 33]
    
    print 'hello not map, ', [add100(i) for i in hh]
    print 'hello 1st, ', map(add100, hh)

simple()

def sec():
    def abc(a, b, c):
        return a * 1000 + b * 100 + c
    
    list1 = [11,22,33]
    list2 = [44,55,66]
    list3 = [77,88,99]
    
    print 'hello sec, ', map(abc, list1, list2, list3)

sec()

def noneFuncMap():
    def one():
        list1 = [11, 22, 33]
        print map(None, list1)
    
    def two():
        list1 = [11,22,33]
        list2 = [44,55,66]
        list3 = [77,88,99]
        
        print map(None,list1,list2,list3)
    
    def three():
        str1 = 'one'
        str2 = 'two'
        str3 = 'three'
        
        print map(None, str1, str2, str3)
    
    one()
    two()
    three()
noneFuncMap()


def abcc():
    def abc(a, b, c):
        return a*10000 + b*100 + c
   
    list1 = [11,22,33]
    list2 = [44,55,66]
    list3 = [77,88,99]
    
    print 'abc func output, ', map(abc,list1,list2,list3)
    
abcc()

        