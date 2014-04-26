'''
Created on 2011-9-23

@author: root
'''
from sys import stdout
import urllib2
from application import log

def sendRequest(url,token):
    print url + token
    req = urllib2.Request(url + token)
    response = urllib2.urlopen(req)
    
    status = response.getcode()
    if  status == 200 :
        for line in response.readlines():
            stdout.write(line)
    else:
        info = response.info()
        log.info("status code %s , info %s" %(status,info));
    response.close()
    

sendRequest('http://baidu.com',"")    #redirect
#sendRequest('http://www.baidu.com/s?wd=',"ss")  #OK 200
#sendRequest('http://www.google.com.hk/search?hl=en&source=hp&biw=&bih=&btnG=Google+Search&q=',"ss") 


