# -*- coding: utf-8 -*-
'''
Created on 2011-9-23
@author: root
'''
import urllib 
def getGoogleMainPage():
    print urllib
    urlConn = urllib.urlopen('http://www.baidu.com')
    google = urlConn.read()

    header = urlConn.info()
    print 'http header:\n', header
    print 'http status:', urlConn.getcode()  
    print 'url:', urlConn.geturl()  
    for line in google: # 就像在操作本地文件  
        print line,  
    urlConn.close()

if __name__ == '__main__':
    getGoogleMainPage()