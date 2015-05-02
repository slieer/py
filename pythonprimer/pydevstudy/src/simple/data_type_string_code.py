# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2015

@author: dev

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
'''

str1 = u'\u52c3\u5229\u53bf'
print str1

s = u'中文' #unicode编码的文字
print s.encode('utf-8')   #转换成utf-8格式输出 

text = eval("u"+"'\u56c3\u67e4'")
print text 

arr0 = [u'可以', u'负数', u'切片', u'序列', u'位置', u'例如', u'返回']
print 'arr0:', arr0

arr = [[]]
arr.append([['新闻'],['贴吧']])
arr.append([['知道'],['音乐']])
arr.append([['图片'],['视频']])

print arr

