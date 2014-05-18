'''
Created on 2011-9-20

@author: slieer
'''
from twisted.web import client
import tempfile

def downloadToTempFile(url):
    """
                传递一个URL，并返回一个Deferred对象用于下载完成时的回调
    """
    tmpfd, tempfilename = tempfile.mkstemp()
    os.close(tmpfd)
    return client.downloadPage(url, tempfilename).addCallback(returnFilename, tempfilename)

def returnFilename(result, filename):
    return filename

if __name__ == '__main__':
    import sys, os
    from twisted.internet import reactor

    def printFile(filename):
        for line in file(filename, 'r+b'):
            sys.stdout.write(line)

        os.unlink(filename) #删除文件
        reactor.stop()

    def printError(failure):
        print >> sys.stderr, "Error: ", failure.getErrorMessage()
        reactor.stop()

    if len(sys.argv) == 2:
        url = sys.argv[1]

        downloadToTempFile(url).addCallback(printFile).addErrback(printError)
        reactor.run()

    else:
        print "Usage: %s <URL>" % sys.argv[0]
