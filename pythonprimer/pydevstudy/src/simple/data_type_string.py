# -*- coding: utf-8 -*-
'''
Created on 2012-7-8
@author: me
'''
import string

def string_view():
    function = []
    variables = []
    
    for fv in dir(string):
        name = "string.%s" % fv
        if callable(eval(name)):
            function.append(fv)
        else:
            variables.append(fv)
    print "fun:", function
    print "----------------------"
    print "var:", variables

def str_test():
    print string.ascii_lowercase
    print string.ascii_uppercase
    print string.ascii_letters
    print string.digits
    print string.hexdigits
    print  string.letters
    print string.octdigits
    print 'a' , 'b'
    #A string containing all characters that are considered whitespace. 
    print string.whitespace

    name = 'Swaroop' '''This is a string object'''
    
    if name.startswith('Swa'):
        print 'Yes, the string starts with "Swa"'
    if 'a' in name :
        print 'Yes, it contains the string "a"'
    if name.find('war') != -1 :
        print 'Yes, it contains string "war"'
    delimiter = '-*-'
    mylist = ['brazil','Russia','India','China']
    print delimiter.join(mylist)

def strTo():
    print float('30.7894')
    print int('7894')


class StrType :
    def __init__(self, st):
        self.st = st
    def test(self):
        print string.swapcase(self.st);
        print string.strip("  blank   ")
        print string.split("hello world")
        print string.join(["a", "b", "c", "d"], ",");
                
if __name__ == '__main__' :
    "str_test()"
    "string_view()"
    strOjb = StrType("ZhaiXiaoBin");
    strOjb.test()
    
    strTo()
    
