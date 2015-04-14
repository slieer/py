# -*- coding: UTF-8 -*-
'''
Created on Apr 13, 2015

@author: dev
'''
import csv
from django.template.defaultfilters import default
from simple.function_class import DefaultParam

def csvTest():
    srcFilePath = open("samples/sample.csv")
    targetFile = open("")
    #从文件读取
    reader = csv.reader(file(srcFilePath,'rb'))  
    
    for line in reader:  
        #忽略第一行  
        if reader.line_num == 1:  
            continue    
        #line是个list，取得所有需要的值  
        type = line[0]  
    
    #写入文件  
    writer = csv.writer(open(targetFile,"wb"),quoting=csv.QUOTE_ALL)  
    #传入list  
    writer.writerow(["121","121"])  
    #传入2纬list  
    writer.writerows([["121","121"]]) 
    
    
def defaltPath():
    import os
    print os.path.abspath(".")
    

if __name__ == '__main__':
    defaltPath()