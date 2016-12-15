'''
Created on May 18, 2015

@author: dev
'''

import yaml
f = open('tree.yaml')
dataMap = yaml.load(f)
f.close()

print dataMap

