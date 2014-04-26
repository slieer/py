# -*- coding: utf-8 -*-
'''
Created on 2011-9-19
http://blog.csdn.net/gashero/article/details/1519045
@author: slieer
'''
from twisted.web import http
def renderHomePage(request):
    colors = 'red', 'blue', 'green'
    flavors = 'vanilla', 'chocolate', 'strawberry', 'coffee'
    request.write("""
    <html>
    <head>
        <title>Form Test</title>
    </head>
    <body>
        <form action="posthandler" method="POST">
            Your Name:
            <p>
                <input type="text" name="name">
            </p>
            What's your favorite color?
            <p>
    """)
    
    for color in colors:
        request.write(
            "<input type='radio' name='color' value='%s'>%s<br/>" % (
            color, color.capitalize()))
    request.write("""
        </p>
        What kinds of ice cream do you like?
        <p>
        """)
    for flavor in flavors:
        request.write(
            "<input type='checkbox' name='flavor' value='%s'>%s<br/>" % (
            flavor, flavor.capitalize()))
    request.write("""
        </p>
        <input type='submit'/>
    </form>
    </body>
    </html>
    """)
    request.finish()
def handlePost(request):
    request.write("""
    <html><head><title>Posted Form Datagg</title>
        </head>
        <body>
        <h1>Form Data</h1>
    """)
    for key, values in request.args.items():
        request.write("<h2>%s</h2>" % key)
        request.write("<ul>")
        for value in values:
            request.write("<li>%s</li>" % value)
        request.write("</ul>")
    request.write("""
        </body></html>
    """)
    request.finish()
class FunctionHandleRequest(http.Request):
    pageHandlers = {
        '/':renderHomePage,        #第一个页面
        '/posthandler':handlePost,      #第二个页面
    }
    def process(self):
        self.setHeader("Content-Type", "text/html")
        if self.pageHandlers.has_key(self.path):
            handler = self.pageHandlers[self.path]
            handler(self)
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such page.")
            self.finish()
class MyHttp(http.HTTPChannel):
    requestFactory = FunctionHandleRequest
    
class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp
if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, MyHttpFactory())
    reactor.run()
