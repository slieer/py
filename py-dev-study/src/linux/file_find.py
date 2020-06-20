#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 16, 2014

@author: slieer
'''

import os


workspace_dir = '/opt/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings'

def findFile(arg, dirname, files):
    if "jboss" in dirname:
            print(dirname)

os.path.walk(workspace_dir, findFile, None)

"""
for i in os.walk(workspace_dir):
    print i
"""
def checksize(arg, dirname, files):
    for f in files:
        filepath = os.path.join(dirname, f)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            if size > 1000000:
                size_in_Mb = size/1000000.0
                arg.append((size_in_Mb, filepath))
def findBySize():
    bigfiles = []
    root = os.environ['HOME']
    os.path.walk(root, checksize, bigfiles)
    for size, name in bigfiles:
        print(name, '大小为', size, 'Mb') 
                    
"""findBySize()"""               