'''
Created on 2011-9-22
@author: slieer

发出一个请求,
'''
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

agent = Agent(reactor)

d = agent.request(
    'GET',
    'http://www.google.com/',
    Headers({'User-Agent': ['Twisted Web Client Example']}),
    None)

def cbResponse(ignored):
    print 'Response received:%s' %ignored

def cbShutdown(ignored):
    reactor.stop()

d.addCallback(cbResponse)
d.addBoth(cbShutdown)

reactor.run()
