#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2012-11-30
@author: slieer
'''
import os
#import popen2

import subprocess


def popen():
    stdout, stdin = subprocess.Popen("ls")
    ostr = stdout.read()
    print ostr


def main():
    os.system('ls')
    os.system('cat /proc/cpuinfo')

"""
[slieer@local ~]$ ls -l --color=auto -h -t --time-style=long-iso | grep '2014-03-09 07:39'
drwxrwxr-x. 2 slieer slieer 4.0K 2014-03-09 07:39 Videos
drwxrwxr-x. 2 slieer slieer 4.0K 2014-03-09 07:39 Music
drwxrwxr-x. 2 slieer slieer 4.0K 2014-03-09 07:39 Pictures
drwxrwxr-x. 2 slieer slieer 4.0K 2014-03-09 07:39 Public
drwxrwxr-x. 2 slieer slieer 4.0K 2014-03-09 07:39 Templates
"""
def main1():
    currDir = '/opt/source-code'
    """设置当前目录"""
    os.chdir(currDir)
    comm = "ls -l --color=auto -h -t --time-style=long-iso | grep \'2013-04-09 00:45\'"
    #os.system(comm)
    
    date = '2013-04-09 00:45'
    delFileComm = 'rm -rf '
    with os.popen(comm) as f:
        for line in f:
            #去掉前后空格
            tmp_str = line.strip() 
            #print tmp_str
            arr = tmp_str.split(date)
            fileName = arr[1].strip()
            print fileName
            
            comm1 = delFileComm + fileName
            print comm1
            os.system(comm1)
                
    
if __name__ == '__main__':
    main1()

# vim:set nu et ts=4 sw=4 cino=>4: