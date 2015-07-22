#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on May 31, 2015

@author: dev
'''
import sys
import unittest
from urlgrabber import urlopen
from urlgrabber.grabber import URLGrabError
from pyquery import PyQuery as pq

import logging

logging.basicConfig(level=logging.DEBUG)

reload(sys)
sys.setdefaultencoding( "utf-8" )

def getHtml(url, showUrl=False):
    if showUrl :
        logging.info(url)    

    try:
        page = urlopen(url)
        html = page.read()
        page.close()
        return html
    except URLGrabError:
        logging.error('exce url:' + url)
    return ""


class Test(unittest.TestCase):


    def testName(self):
        url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/34/3413.html'
        html = getHtml(url, True)
        #logging.info('html:' + html)
        d = pq(html)
        table = d.find('table.countytable')
        logging.info(table)
        trList = table.find('tr')
        for tr in trList :
            logging.info(tr)
        
    def testTr(self):
        html = """
    <table class='countytable'>
    <tr class='countyhead'>
    <td width=150>代码</td><td>名称</td></tr>
    <tr class='countytr'><td>341301000000</td><td>市辖区</td></tr>
    <tr class='countytr'><td><a href='13/341302.html'>341302000000</a></td><td><a href='13/341302.html'>埇桥区</a></td></tr>
    <tr class='countytr'><td><a href='13/341321.html'>341321000000</a></td><td><a href='13/341321.html'>砀山县</a></td></tr>
    <tr class='countytr'><td><a href='13/341322.html'>341322000000</a></td><td><a href='13/341322.html'>萧县</a></td></tr>
    <tr class='countytr'><td><a href='13/341323.html'>341323000000</a></td><td><a href='13/341323.html'>灵璧县</a></td></tr>
    <tr class='countytr'><td><a href='13/341324.html'>341324000000</a></td><td><a href='13/341324.html'>泗县</a></td></tr>
    </table>
    """
        p = pq(html)
        trList = p.find('tr')
        for tr in trList:
            logging.info(tr)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()