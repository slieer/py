# -*- coding: utf-8 -*-

'''
Created on 2011-9-20
@author: slieer
'''
from twisted.web import resource, static, server
class ColorPage(resource.Resource):
    def __init__(self, color):
        self.color = color
    def render(self, request):
        return """
        <html>
        <head>
            <title>Color: %s</title>
            <link type='text/css' href='/styles.css' rel='Stylesheet' />
        </head>
        <body style='background-color: #%s'>
            <h1>This is #%s.</h1>
            <p style='background-color: white'>
            <a href='/color/'>Back</a>
            </p>
        </body>
        </html>
        """ % (self.color, self.color, self.color)
class ColorRoot(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.requestedColors = []
        self.putChild('', ColorIndexPage(self.requestedColors))
    def render(self, request):
        # redirect /color -> /color/
        request.redirect(request.path + '/')
        return 'please use /colors/ instead.'
    def getChild(self, path, request):
        if path not in self.requestedColors:
            self.requestedColors.append(path)
        return ColorPage(path)
    
class ColorIndexPage(resource.Resource):
    def __init__(self, requestedColorsList):
        resource.Resource.__init__(self)
        self.requestedColors = requestedColorsList
    def render(self, request):
        request.write("""
        <html>
        <head>
          <title>Colors</title>
          <link type='text/css' href='/styles.css' rel='Stylesheet' />
        </head>
        <body>
        <h1>Colors</h1>
        To see a color, enter a url like
        <a href='/color/ff0000'>/color/ff0000</a>. <br />
        Colors viewed so far:
        <ul>""")
        for color in self.requestedColors:
            request.write(
                "<li><a href='%s' style='color: #%s'>%s</a></li>" % (
                color, color, color))
        request.write("""
        </ul>
        </body>
        </html>
        """)
        return ""
class HomePage(resource.Resource):
    def render(self, request):
        return """
        <html>
        <head>
            <title>Colors</title>
            <link type='text/css' href='/styles.css' rel='Stylesheet' />
        </head>
        <body>
        <h1>Colors Demo</h1>
        What's here:
        <ul>
            <li><a href='/color'>Color viewer</a></li>
        </ul>
        </body>
        </html>
        """
if __name__ == '__main__':
    from twisted.internet import reactor
    root = resource.Resource()
    root.putChild('', HomePage())
    root.putChild('color', ColorRoot())
    root.putChild('styles.css', static.File('styles.css'))
    site = server.Site(root)
    reactor.listenTCP(8000, site)
    reactor.run()
