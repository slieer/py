# -*- coding: utf-8 -*-

'''
Created on 2015年12月1日
@author: sdt12546
'''
import random
from jinja2 import Template

token = 'LCsKkH4dE8gQ4O3wqNZY-6E8eE5RdyhQq7jconL42yULEaHjyWpmC0oVulTK4wpO'
urlTpl = 'http://mifeng.skyworthbox.com/api/video2.0/video_play.action?videoInfoId={{videoId}}&bqsPassport={{token_}}'
def getTplStr(vid):
    template = Template(urlTpl) 
    return template.render(token_=token, videoId=vid) 
    
def fun():
    
    output = open('data.txt', 'a')
    for i in range(1, 10):
        i = random.randint(1, 300000)
        test = getTplStr(i)
        output.write(test + "\n")
    
    output.close()    
if __name__ == '__main__':
    fun()
