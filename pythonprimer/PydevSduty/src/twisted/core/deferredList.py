'''
Created on 2011-9-27

@author: root
'''
from twisted.internet import defer

def got_results(res):
    print 'We got:', res

class DeferredTest:

    def test(self):
        print 'Empty List.'
        d = defer.DeferredList([])
        print 'Adding Callback.'
        d.addCallback(got_results)

    def test1(self):        
        print 'One Deferred.'
        d1 = defer.Deferred()
        d = defer.DeferredList([d1])
        print 'Adding Callback.'
        d.addCallback(got_results)
        print 'Firing d1.'
        d1.callback('d1 result')
        
        
a = DeferredTest()
#a.test()
a.test1()



