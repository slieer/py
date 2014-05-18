'''
Created on 2011-9-24

@author: root
'''
from twisted.internet import reactor
from twisted.web import static, server
from twisted.web import resource

PORT = 8080

class First( resource.Resource):
    def render(self, request):
        return 'helloworld!' 

index = resource.Resource()
index.putChild('hello', First())   #request http://localhost:8080/hello
index.putChild('', static.File('index.html'))    #request http://localhost:8080/
                                                                           
reactor.listenTCP(PORT, server.Site(index))
reactor.run()