# -*- coding: utf-8 -*-
'''
Created on 2010-6-27

@author: me
'''
def basicFor():
    for i in range(1, 5) :
        print i
    else :
        print "The for loop is over."   

def basicFor1():
    for i in range(1, 5, 2) :
        print i
    else :
        print "The for loop is over."   


"""tuple for in"""
def tupleFor():
    x = [{'xhtml', 'css'}, {'javascript', 'python'}]
    for (a, b) in x:
        print (a, b)
        print a[0]  #表示字符串数组的第一个字符

def forElseTest() :
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n / x
                break
            else:
                # loop fell through without finding a factor
                print n, 'is a prime number'

if __name__ == '__main__':   
    #basicFor()
    basicFor1()
    tupleFor()
