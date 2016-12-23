#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on May 11, 2014

@author: root
'''
import os

centos_dvd_dir = '/opt/os/CentOS-6.5-x86_64-bin-DVD1/Packages/'
u_dir = '/media/CENTOS_6.5_/Packages'

'''
dve_dir = open(centos_dvd_dir, mode='r')
u_dir = open(u_dir, mode='r')

IOError: [Errno 21] Is a directory:
'''

dvd_list = os.listdir(centos_dvd_dir)
u_list = os.listdir(u_dir)

print("---dif---")
for x in dvd_list:
    flag = False
    for y in u_list:
        if x == y :
            flag = True
            continue
    if(not flag) :
        print(x)