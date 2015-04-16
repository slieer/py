#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Apr 13, 2015
@author: Zhai Xiaobin

create table data(
code,
area_name,
level,

)

根据《规定》，统计上划分城乡的类别分为：
100 城镇
110 城区
111 主城区
112 城乡结合区
120 镇区
121 镇中心区
122 镇乡结合区
123 特殊区域
200 乡村
210 乡中心区
220 村庄
'''

import sys
import csv
import os
from urlgrabber import urlopen
from urlgrabber.grabber import URLGrabError

from pyquery import PyQuery as pq
#d = pq("<html></html>")
#d = pq(etree.fromstring("<html></html>"))
#d = pq(url=your_url, opener=lambda url, **kw: urlopen(url).read())
#d = pq(filename=path_to_html_file)

reload(sys)
sys.setdefaultencoding( "utf-8" )
gov_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/'

def getHtml(url, showUrl=False):
    if showUrl :
        print url    

    try:
        page = urlopen(url)
        html = page.read()
        page.close()
        return html
    except URLGrabError:
        print 'exce url', url
    return ""    


def getAreaList(urlPrev, linkArr, nodeClass,level, classback=None):
        #rint linkArr
    linkPq = []
    for link in linkArr :
        url = urlPrev
        #print  url
        if classback:
            url = url + classback(link) + '/'
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
                                
                arr = [arr1.text(), arr2.text(), level, ""]
                csvWrite(arr)
         
    return linkPq

parentPath = os.environ['HOME'] + '/Documents/'
writer = csv.writer(open(parentPath + 'data.csv',"wb"), quoting=csv.QUOTE_ALL)  
def csvWrite(arr):
    #写入文件  
    #传入list  
    writer.writerow(arr)  
    #传入2纬list  
    #writer.writerows([["121","121"]])     
    
    
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
        arr = [url[0:-5], linkPq.text(), 1, ""]
        csvWrite(arr)
        
    return linkArr

def getCity(linkArr):
    
    return getAreaList(gov_url ,linkArr, 'TR.citytr', 2)
    
def getCountytr(linkArr):
    return getAreaList(gov_url, linkArr, 'TR.countytr', 3)
    
def getTowntr(linkArr):
    #data = '01/110102.html'    
    def partStrFunc(data):
        arr = data.split('/')
        #print arr[1][0:2]
        return arr[1][0:2]

    return getAreaList(gov_url, linkArr,'TR.towntr',4, partStrFunc)

def getVillagetr(linkArr):
    def partStrFunc(data):
        arr = data.split('/')
        #print arr[1][0:2]
        return arr[1][0:2] + '/' + arr[1][2:4] + '/'
    
    #    for link in linkArr :
    #        part = partStrFunc(link)
    #        url = gov_url + part + link
    #        print url
        return getAreaList(gov_url, linkArr, 'TR.villagetr', 5, partStrFunc)
    
    
def data():
    html = getHtml(gov_url + 'index.html')
    
    cityLinks = getPrivince(html)
    print 'privince end---------------------------------------------------'
    countryLinks = getCity(cityLinks)
    print 'city end---------------------------------------------------'
    #print countryLinks
    townLinks = getCountytr(countryLinks)
    print 'countr end---------------------------------------------------'
    
    villageLinks = getTowntr(townLinks)
    print 'town end---------------------------------------------------'

    getVillagetr(villageLinks)

def villageDataTest():   
    townLinks = ['01/110102.html', '01/110105.html', '01/110106.html', '01/110107.html']
    villageLinks = getTowntr(townLinks)
    print 'town end---------------------------------------------------'

    getVillagetr(villageLinks)


if __name__ == '__main__':
    #getPrivince() #"http://sina.com.cn"
    #villageDataTest()
    data()

    
