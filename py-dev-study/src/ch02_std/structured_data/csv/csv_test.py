# -*- coding: UTF-8 -*-
'''
Created on Apr 13, 2015

@author: dev
'''
import os
import csv

parentPath = os.environ['HOME'] + '/Documents/'

def csvReadTest():
    srcFilePath = open(parentPath + "sample.csv")
    print(srcFilePath)
    #从文件读取
    reader = csv.reader(srcFilePath)  
    
    for line in reader:  
        #忽略第一行  
        print(line)
        
def csvWriteTest():
    #写入文件  
    writer = csv.writer(open(parentPath + 'data.csv',"wb"), quoting=csv.QUOTE_ALL)  
    #传入list  
    writer.writerow(["121","121"])  
    #传入2纬list  
    writer.writerows([["121","121"]]) 
    
    
def defaltPath():
    print(os.path.abspath("."))
    print(os.environ['HOME'])

    print(os.path.expandvars('$HOME'))
    print(os.path.expanduser('~'))
    

if __name__ == '__main__':
    #defaltPath()
    csvReadTest()
    csvWriteTest()