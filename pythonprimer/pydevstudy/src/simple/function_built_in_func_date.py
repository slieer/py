# -*- coding: utf-8 -*-
'''
Created on 2012-10-7

@author: me
'''
from simple._hello_world_v1 import Basic
b = Basic()

from datetime import datetime     
from datetime import date
import time

def dateTest(): 
        print 'date.max:', date.max
        print 'date.min:', date.min
        today = date.today()
        print 'date.today():', today
        print 'date.fromtimestamp():', date.fromtimestamp(time.time())

def dateTest1():
        now = date(2012, 10, 07)
        tomorrow = now.replace(day = 07)
        print 'now =%s, tomorrow: %s' %(now,tomorrow)
        print 'timetuple():', now.timetuple()
        print 'weekday():', now.weekday()
        print 'isoweekday():', now.isoweekday()
        print 'isocalendar():', now.isocalendar()
        print 'isoformat():', now.isoformat()

def dateTest2():
        print 'datetime.resolution:', datetime.resolution
        print 'today():', datetime.today()
        print 'now():', datetime.now()
        print 'utcnow():', datetime.utcnow()
        print 'fromtimestamp(tmstmp):', datetime.fromtimestamp(time.time())
        print 'utcfromtimestamp(tmstmp):', datetime.utcfromtimestamp(time.time())
        print 'timetuple:', datetime.now().timetuple()
        print 'utctimetuple:',datetime.now().utctimetuple()
        print 'toordinal', datetime.now().toordinal()
        print  'isocalendar:',datetime.now().isocalendar()
        print 'ctime:', datetime.now().ctime()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')

def dateTest3():
        pass
if __name__ == '__main__' :
        #dateTest1()        
        dateTest2()        

