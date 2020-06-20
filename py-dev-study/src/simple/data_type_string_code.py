# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2015

@author: dev

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
'''

def str_():
    str1 = '\u52c3\u5229\u53bf'
    print(str1)
    
    s = '中文' #unicode编码的文字
    print(s.encode('utf-8'))   #转换成utf-8格式输出 
    
    text = eval("u"+"'\\u56c3\\u67e4'")
    print(text) 

def arr():
    one_dim_arr = ['可以', '负数', '切片', '序列', '位置', '返回']
    print('one_dim_arr:', one_dim_arr)
    
    for element in one_dim_arr:
        print(element)
    
    two_dimensional_arr = []
    two_dimensional_arr.append(['新闻', '贴吧'])
    two_dimensional_arr.append(['知道', '音乐'])
    two_dimensional_arr.append(['图片', '视频'])
    
    print('two_dimensional_arr:',two_dimensional_arr)
    
    for el in two_dimensional_arr:
        print(el)

arr()