'''
Created on 2012-11-30

@author: slieer
'''

import threading

class TestThread(threading.Thread):

    def __init__(self, name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0

        threading.Thread.__init__(self, name=name)

    def run(self):
        """ main control loop """
        print "%s starts" % (self.getName(),)

        count = 0
        while not self._stopevent.isSet():
            count += 1
            print "loop %d" % (count,)
            self._stopevent.wait(self._sleepperiod)

        print "%s ends" % (self.getName(),)

    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)

if __name__ == "_ _main_ _":
    testthread = TestThread()
    testthread.start()

    import time
    time.sleep(10.0)

    testthread.join()