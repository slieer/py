# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Created on 2011-9-11
@author: me
Chapter 1 - Download Example

test example:
    python Chp1AdvDownloadClient.py http://www.rfc-editor.org/rfc/rfc6120.txt
'''
import urllib 
from sys import argv
from sys import stdout

f = urllib.urlopen(argv[1])
while 1:
    buf = f.read(2048)    
    if not len(buf):
        break
    stdout.write(buf)



