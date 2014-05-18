'''
Created on 2011-9-11

@author: me
'''
import sys,urllib2

myurl = 'www.baidu.com'
#myurl = sys.argv[1]
if not myurl.startswith("http://"):
    myurl = ''.join(['http://' ,myurl])

req = urllib2.Request(myurl)
fd = urllib2.urlopen(req)

print "Retrieved " ,fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" %(key, value)

print "--------------------------------------"

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
    
    