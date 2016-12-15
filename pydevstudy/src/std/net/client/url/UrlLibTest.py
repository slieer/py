# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Created on 2011-9-23
@author: root
'''
import urllib 
def getGoogleMainPage():
    #print urllib
    urlConn = urllib.urlopen('http://www.baidu.com')
    google = urlConn.read()

    header = urlConn.info()
    print 'http header:\n', header
    print 'http status:', urlConn.getcode()  
    print 'url:', urlConn.geturl()  
    for line in google: # 就像在操作本地文件  
        print line,  
    urlConn.close()

'''
Created on 2011-9-11
@author: me
Chapter 1 - Download Example

test example:
    python Chp1AdvDownloadClient.py http://www.rfc-editor.org/rfc/rfc6120.txt
'''
def getUrlToconsole():
    from sys import argv
    from sys import stdout
    
    f = urllib.urlopen(argv[1])
    while 1:
        buf = f.read(2048)    
        if not len(buf):
            break
        stdout.write(buf)

if __name__ == '__main__':
    getGoogleMainPage()