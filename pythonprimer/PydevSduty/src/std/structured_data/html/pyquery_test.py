#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Mar 29, 2015
@author: dev
'''
from pyquery import PyQuery as pq
#d = pq("<html></html>")
#d = pq(etree.fromstring("<html></html>"))
#d = pq(url=your_url, opener=lambda url, **kw: urlopen(url).read())
#d = pq(filename=path_to_html_file)
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
"""
gov_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html'
def getPrivince(html):
    d = pq(html)
    #print d.find('head meta')
    
    links = d.find('A')
    for link in links :
        #print link
        linkPq = pq(link)
        print linkPq.attr('href'), linkPq.text()
        #.decode('gb2312', 'ignore').encode('utf-8')
 
def getHtml(url): 
    from urlgrabber import urlopen
    page = urlopen(url)
    html = page.read()
    page.close()
    return html    
          
if __name__ == '__main__':
    #getPrivince() #"http://sina.com.cn"
    html = getHtml(gov_url)
    getPrivince(html)
    
    
    