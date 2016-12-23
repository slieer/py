#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2012-11-30
@author: slieer
'''
def ifTest():
    print(type( "" ))
    if type( "I am a string" ) is str: 
        print(True)
    if type( "Another string" ) is str(): 
        print(True)


def arrTest():
    tokens = "This is a sample string used to demo split()".split()
    len(tokens)
    print(tokens)
    print(tokens[0], tokens[2])

    print(tokens[-1], tokens[-2])
    print(tokens[2:5])
    
def main():
    print("Hello, world")

if __name__ == '__main__':
    main()
    ifTest()
    arrTest()

# vim:set nu et ts=4 sw=4 cino=>4:
