# -*- coding: utf-8 -*-
'''
Created on 2012-7-8
@author: me

# vim:set nu et ts=4 sw=4 cino=>4:
'''
import string
import collections

def str_():
    str1 = '\u52c3\u5229\u53bf'
    print(str1)
    
    s = '中文' #unicode编码的文字
    print(s.encode('utf-8'))   #转换成utf-8格式输出 
    
    text = eval("u"+"'\\u56c3\\u67e4'")
    print(text) 


def ifTest():
    print(type( "" ))
    if type( "I am a string" ) is str: 
        print(True)
    if type( "Another string" ) is str(): 
        print(True)


def arrTest():
    tokens = "This is a sample string used to demo split()".split()
    len(tokens)
    print(tokens)
    print(tokens[0], tokens[2])

    print(tokens[-1], tokens[-2])
    print(tokens[2:5])
    
def string_view():
    function = []
    variables = []
    
    for fv in dir(string):
        name = "string.%s" % fv
        if isinstance(eval(name), collections.Callable):
            function.append(fv)
        else:
            variables.append(fv)
    print("fun:", function)
    print("----------------------")
    print("var:", variables)

def str_test():
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.ascii_letters)
    print(string.digits)
    print(string.hexdigits)
    print(string.ascii_letters)
    print(string.octdigits)
    print('a' , 'b')
    #A string containing all characters that are considered whitespace. 
    print(string.whitespace)

    name = 'Swaroop' '''This is a string object'''
    
    if name.startswith('Swa'):
        print('Yes, the string starts with "Swa"')
    if 'a' in name :
        print('Yes, it contains the string "a"')
    if name.find('war') != -1 :
        print('Yes, it contains string "war"')
    delimiter = '-*-'
    mylist = ['brazil','Russia','India','China']
    print(delimiter.join(mylist))

def strTo():
    print(float('30.7894'))
    print(int('7894'))

    #字符串反转
    #实现更好编码的 30 个神奇的 Python 技巧
    #https://www.infoq.cn/article/BrYVP5bLfE4QGqQEAGF1
    my_string = "MY STRING"
    rev_string = my_string[::-1]
    print(rev_string)

class StrType :
    def __init__(self, st):
        self.st = st
    def test(self):
        print(self.st)
                
if __name__ == '__main__' :
    "str_test()"
    "string_view()"
    strOjb = StrType("ZhaiXiaoBin")
    strOjb.test()    
    strTo()
    ifTest()
    arrTest()

    
