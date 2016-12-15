#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Apr 18, 2015
@author: dev
'''

import httplib2
import HTMLParser
import logging

logging.basicConfig(level=logging.INFO)

class DataParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.taglevels=[]
        self.processing=None
        HTMLParser.HTMLParser.__init__(self)
        
        self.attr_id = '';
        self.title = ''
        self.class_ = ''
        self.is_table_tag = False
        
        self.result_list = []
        
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            self.data=''
            self.processing=tag
            
            for attr in attrs:
                if 'title' in attr:
                    self.title = attr[1]
                if 'class' in attr :
                    self.class_ = attr[1]
                if 'id' in attr:
                    self.id = attr[1]            
            
    def handle_data(self,data):
        if self.processing:
            self.data += data
            
    def handle_endtag(self,tag):                
        if tag == self.processing\
            and self.get_data() != '查看'\
            and self.class_ == 'iView'\
            and self.id != '':
            
            #print str(self.id)
            self.result_list.append(self.id)
            
            self.processing=None
        
        self.attr_id = '';
        self.title = ''
        self.class_ = ''
            
    def get_data(self):
        return self.data

import std.structured_data.html.china_break_mongo as mongoTest

h =httplib2.Http()
def getDetailData():
    max_page = 12802
    max_page = 2
    shixinUrl = 'http://shixin.court.gov.cn/unitMore.do?currentPage='
    detail_url = 'http://shixin.court.gov.cn/detail?id='
    for i in range(1, max_page):
        resp = h.request(shixinUrl + str(i))
        content = resp[1]
        #print content
        tp = DataParser()
        tp.feed(content)
        
        for detail_id in tp.result_list:
            req_url = detail_url + detail_id
            content = h.request(req_url)[1]
            logging.info(content)
            
            #contentJson[]
            mongoTest.insert(content)
        
def test():
    shixinUrl = 'http://shixin.court.gov.cn/unitMore.do?currentPage=1'
    detail_url = 'http://shixin.court.gov.cn/detail?id='
    resp, content = h.request(shixinUrl)
    print resp.status
    print resp
    
    tp = DataParser()
    tp.feed(content)
        
    #print tp.result_list
    
    for detail_id in tp.result_list:
        req_url = detail_url + detail_id
        resp, content = h.request(req_url)
        print content
        
if __name__ == '__main__':
    getDetailData()
    #test()
    
