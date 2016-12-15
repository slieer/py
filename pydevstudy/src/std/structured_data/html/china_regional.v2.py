#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Apr 13, 2015
@author: Zhai Xiaobin

create table data(
code,
area_name,
level,
village_level
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

reload(sys)
sys.setdefaultencoding( "utf-8" )
gov_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/'

class AreaLevel:
    privince_level = 1
    city_level = 2
    county_level = 3
    town_level = 4
    village_level = 5


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
        print url
        d = pq(getHtml(url))
        trList = d.find(nodeClass)
        print trList
        
        result_arr_list = [[]]
        for tr in trList :
            code = 0
            name = ''
            village_level_code = 0
            if(level != AreaLevel.village_level):
                arr = pq(tr).find('A')
                if(arr.length == 2) :
                    #print 'A node'
                    arr1 = pq(arr[0])
                    arr2 = pq(arr[1])  
                    url = arr1.attr('href')
                    linkPq.append(url)
                                    
                    code = arr1.text() 
                    name = arr2.text()
                else:
                    #print 'td node'
                    arr = pq(tr).find('td')
                    if(arr.length == 2):
                        code = pq(arr[0]).text()
                        name = pq(arr[1]).text()
            else:
                #leaf node.
                arr = pq(tr).find('td')
                                
                code = pq(arr[0]).text()
                village_level_code= pq(arr[1]).text() 
                name = pq(arr[2]).text()
            
            result_arr = [int(code), name, level, int(village_level_code)]
            csvWrite(result_arr)
            #result_arr_list.append(result_arr)
        #print result_arr_list
        #csvWrite(result_arr_list)

    return linkPq

parentPath = os.environ['HOME'] + '/Documents/data_test_county.v1.csv'
writer = csv.writer(open(parentPath, "wb"), quoting=csv.QUOTE_NONNUMERIC)  
def csvWrite(arr):
    writer.writerow(arr)    
    
def getPrivinceList(html):
    d = pq(html)
    
    linkArr = []
    links = d.find('TR.provincetr').find('A')
    for link in links :
        linkPq = pq(link)
        url = linkPq.attr('href')
        linkArr.append(url)
        arr = [int(url[0:-5]), linkPq.text(), AreaLevel.privince_level, 0]
        csvWrite(arr)
        
    return linkArr

def getCityList(linkArr):
    return getAreaList(gov_url ,linkArr, 'TR.citytr', AreaLevel.city_level)
    
def getCountyList(linkArr):
    return getAreaList(gov_url, linkArr, 'TR.countytr', AreaLevel.county_level)
    
def getTownList(linkArr):
    #data = '01/110102.html'    
    def partStrFunc(data):
        arr = data.split('/')
        #print arr[1][0:2]
        return arr[1][0:2]

    return getAreaList(gov_url, linkArr,'TR.towntr', AreaLevel.town_level, partStrFunc)

def getVillageList(linkArr):
    def partStrFunc(data):
        arr = data.split('/')
        #print arr[1][0:2]
        return arr[1][0:2] + '/' + arr[1][2:4] + '/'
    
    #    for link in linkArr :
    #        part = partStrFunc(link)
    #        url = gov_url + part + link
    #        print url
    return getAreaList(gov_url, linkArr, 'TR.villagetr', AreaLevel.village_level, partStrFunc)
    
def data():
    html = getHtml(gov_url + 'index.html')
    
    cityLinks = getPrivinceList(html)
    print 'privince end---------------------------------------------------'
    countryLinks = getCityList(cityLinks)
    print 'city end---------------------------------------------------'
    #print countryLinks
    townLinks = getCountyList(countryLinks)
    print 'countr end---------------------------------------------------'
    
    villageLinks = getTownList(townLinks)
    print 'town end---------------------------------------------------'

    getVillageList(villageLinks)
    
def countyDataTest():
    countryLinks = ['34/3413.html']
    getCountyList(countryLinks)
    
def villageDataTest():   
    townLinks = ['01/110102.html', '01/110105.html', '01/110106.html', '01/110107.html']
    villageLinks = getTownList(townLinks)
    print 'town end---------------------------------------------------'

    getVillageList(villageLinks)


if __name__ == '__main__':
    #getPrivinceList() #"http://sina.com.cn"
    #villageDataTest()
    #data()
    countyDataTest()

    
