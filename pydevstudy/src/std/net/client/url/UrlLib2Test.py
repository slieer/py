'''
Created on 2011-9-23

@author: root
'''
import sys
from sys import stdout
import urllib.request, urllib.error, urllib.parse
import logging as log

def getRequestInfo():
    myurl = 'www.baidu.com'
    #myurl = sys.argv[1]
    if not myurl.startswith("http://"):
        myurl = ''.join(['http://' ,myurl])
    
    response = urllib.request.Request(myurl)
    fd = urllib.request.urlopen(response)
    
    print("Retrieved " ,fd.geturl())
    info = fd.info()
    for key, value in list(info.items()):
        print("%s = %s" %(key, value))
    
    print("--------------------------------------")
    
    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        sys.stdout.write(data)

def getRequest(url):
    print(url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    
    status = response.getcode()
    if  status == 200 :
        for line in response.readlines():
            stdout.write(line)
    else:
        info = response.info()
        log.info("status code %s , info %s" %(status,info));
    response.close()
    

getRequest('http://baidu.com',"")    #redirect
#sendRequest('http://www.baidu.com/s?wd=',"ss")  #OK 200
#sendRequest('http://www.google.com.hk/search?hl=en&source=hp&biw=&bih=&btnG=Google+Search&q=',"ss") 


