# -*- coding: utf-8 -*-
'''
Created on 2010-7-10

@author: me
'''
import time

try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line, end=' ')
finally:
    f.close()
    print('Cleaning up...closed the file') 