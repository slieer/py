'''
Created on Apr 16, 2014

@author: root
'''
from collections import Counter

def counter() :    
    cnt = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue'] :
        cnt[word] += 1
    print cnt
    
import urllib2
def getWordStatTest():
    url = 'https://docs.python.org/2/library/collections.html'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    status = response.getcode()
    if  status == 200 :
        cnt = Counter()
        for line in response.readlines() :
            for word in line.split() :
               cnt[word] += 1
         
        print cnt    
    else:
        info = response.info()
        log.info("status code %s , info %s" %(status,info));
    response.close()

counter()
getWordStatTest()


from collections import OrderedDict  
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}  
print OrderedDict(sorted(d.items(), key=lambda t: t[0]))

