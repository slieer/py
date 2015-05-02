#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Apr 18, 2015
@author: dev
'''

import httplib2
import HTMLParser
h =httplib2.Http()
    
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
    
class DetailDataParser(HTMLParser.HTMLParser):
    pass

if __name__ == '__main__':
    shixinUrl = 'http://shixin.court.gov.cn/unitMore.do?currentPage=100000000'
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
    
    
