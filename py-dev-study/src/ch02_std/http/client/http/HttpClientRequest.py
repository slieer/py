#coding=utf-8   
'''
Created on 2011-9-12

@author: me
'''
import http.client

def testConn():
    conn = http.client.HTTPConnection('www.baidu.com')
    conn.request('GET', '/', headers = {
        "User-Agent" : "ming",
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip,deflate",
    })
    
    print(conn.getresponse().status)
    conn.close()

testConn()


def testHttp():
    conn = http.client.HTTPConnection("www.g.cn", 80, False)
    conn.request('get', '/', headers = {"Host": "www.google.cn",
                                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                                        "Accept": "text/plain"})
    res = conn.getresponse()
    print('version:', res.version)
    print('reason:', res.reason)
    print('status:', res.status)
    print('msg:', res.msg)
    print('headers:', res.getheaders())
    #html
    #print '\n' + '-' * 50 + '\n'
    #print res.read()
    conn.close() 
    