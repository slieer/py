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
if __name__ == '__main__':
    main()

# vim:set nu et ts=4 sw=4 cino=>4: