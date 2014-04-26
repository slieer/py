'''
Created on 2011-3-14

@author: me
'''
import threading

class AsyncZip(threading.Thread):
    i = 10
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        self.i = self.i + 1

background = (AsyncZip(),AsyncZip());
background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'
