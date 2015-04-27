#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Apr 18, 2015

@author: dev
'''


shixinUrl = 'http://shixin.court.gov.cn/unitMore.do?currentPage=1'
#-- coding: GBK --
#coding=utf8
import httplib2
#获取HTTP对象
h =httplib2.Http()
#发出同步请求，并获取内容
resp, content = h.request(shixinUrl)
print resp
print content