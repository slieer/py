'''
Created on 2011-9-22

@author: slieer
'''
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

from stringprod import StringProducer

agent = Agent(reactor)
body = StringProducer("hello, world")
d = agent.request(
    'GET',
    'http://www.google.com/',
    Headers({'User-Agent': ['Twisted Web Client Example'],
             'Content-Type': ['text/x-greeting']}),
    body)

def cbResponse(ignored):
    print 'Response received'
d.addCallback(cbResponse)

def cbShutdown(ignored):
    reactor.stop()
d.addBoth(cbShutdown)

reactor.run()
