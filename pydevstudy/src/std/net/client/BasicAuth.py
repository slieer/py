'''
Created on 2011-9-20

@author: slieer
'''
import urllib2
import sys
import base64 

theurl = 'http://api.minicloud.com.cn/statuses/friends_timeline.xml' 

username = 'qleelulu'
password = 'XXXXXX'  # 你信这是密码吗？ 

base64string = base64.encodestring(
                '%s:%s' % (username, password))[:-1] #注意哦，这里最后会自动添加一个\n
authheader = "Basic %s" % base64string

req = urllib2.Request(theurl)
req.add_header("Authorization", authheader)
try:
    handle = urllib2.urlopen(req)
except IOError, e:
    # here we shouldn't fail if the username/password is right
    print "It looks like the username or password is wrong."
    sys.exit(1)
thepage = handle.read() 
