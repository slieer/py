'''
Created on Apr 27, 2014

@author: root
'''
import unittest
import sys

def redirectOut():
    print "dive in"
    
    #始终在重定向 stdout 之前保存它，这样你可以在后面将其设回正常。
    saveout = sys.stdout
    fsock = open('redirect-out.log', 'w')
    
    #将所有后续的输出重定向到我们刚打开的新文件上。
    sys.stdout = fsock
    print 'This message will be logged instead of displayed'
    
    sys.stdout = saveout
    fsock.close()
    


class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()