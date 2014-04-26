# -*- coding: utf-8 -*-
'''
Created on 2011-9-19
http://blog.csdn.net/gashero/article/details/1519045

'''
from twisted.web import http
class MyRequestHandler(http.Request):
    pages = {
        '/':'<h1>Home</h1>Home Page',  #第一个页面
        '/test':'<h1>Test</h1>Test Page',  #第二个页面
        }
    def process(self):
        if self.pages.has_key(self.path):
            self.write(self.pages[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such page.")
        self.finish()
        
class MyHttp(http.HTTPChannel):
    requestFactory = MyRequestHandler
    
class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp
    
if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, MyHttpFactory())
    reactor.run() #by gashero
