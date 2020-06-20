#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2012-11-30
@author: slieer
'''
import os
import shutil

def fileName():
    try:
        shutil.copy('data.txt', 'data.new.txt')
        os.rename('data.txt', 'data.alter.txt')
        
        os.unlink('data.new.txt')
        shutil.move('data.alter.txt', 'data.txt')
    except IOError as e : 
        print(e)

def filePath():
    f = "data.txt"
    print(shutil.abspath(f))
    
    print(os.path.exists(""))
    print(os.path.isfile(f))
    print(os.path.isdir(f))
    print(os.path.islink(f)) 
    print(os.path.isabs(f))

    print(os.path.split( "a/b/c" ))
    print(os.path.join( "a", "b", "c" ))
    print(os.path.splitext( "dir/file.ext" ))

def main():
    #fileName()
    filePath()
if __name__ == '__main__':
    main()

# vim:set nu et ts=4 sw=4 cino=>4: