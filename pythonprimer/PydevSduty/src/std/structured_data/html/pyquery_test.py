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
gov_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/'

def getHtml(url, showUrl=False):
    if showUrl :
        print url    

    from urlgrabber import urlopen
    from urlgrabber.grabber import URLGrabError
    try:
        page = urlopen(url)
        html = page.read()
        page.close()
        return html
    except URLGrabError:
        print 'exce url', url
    return ""    


def getAreaList(urlPrev, linkArr, nodeClass, isShowUrl=False):
        #rint linkArr
    linkPq = []
    for link in linkArr :
        url = urlPrev
        #print  url
        if isShowUrl:
            url = url + partStr(link) + '/'
            #print 'this url:',partStr(link), ',,', url
        url = url + link
        
        d = pq(getHtml(url))
        trList = d.find(nodeClass)
        
        for tr in trList :
#            print tdList.length

            arr = pq(tr).find('A')
            if(arr.length == 2) :
                arr1 = pq(arr[0])
                arr2 = pq(arr[1])  
                url = arr1.attr('href')
                linkPq.append(url)
                                
                print arr1.text(), arr2.text()
         
    return linkPq

def getPrivince(html):
    d = pq(html)
    #print d.find('head meta')
    
    linkArr = []
    links = d.find('TR.provincetr').find('A')
    for link in links :
        #print link
        linkPq = pq(link)
        url = linkPq.attr('href')
        linkArr.append(url)
        print url[0:-5], linkPq.text()
    return linkArr

def getCity(linkArr):
    
    return getAreaList(gov_url ,linkArr, 'TR.citytr')
    
def getCountytr(linkArr):
    return getAreaList(gov_url, linkArr, 'TR.countytr')
    
def getTowntr(linkArr):
    return getAreaList(gov_url, linkArr,'TR.towntr', True)

def getVillagetr(linkArr):
    'TR.villagetr'
    pass
    
def data():
    html = getHtml(gov_url + 'index.html')
    
    cityLinks = getPrivince(html)
    print 'privince end---------------------------------------------------'
    countryLinks = getCity(cityLinks)
    print 'city end---------------------------------------------------'
    #print countryLinks
    townLinks = getCountytr(countryLinks)
    print 'countr end---------------------------------------------------'
    
    #print townLinks
    getTowntr(townLinks)
    print 'town end---------------------------------------------------'

#data = '01/110102.html'    
def partStr(data):
    arr = data.split('/')
    #print arr[1][0:2]
    return arr[1][0:2]

if __name__ == '__main__':
    #getPrivince() #"http://sina.com.cn"
    data()
    