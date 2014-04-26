'''
Created on 2010-7-4

@author: me

不需要导入
import string
print dir(string)
'''

name = 'Swaroop' '''This is a string object'''

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'
if 'a' in name :
    print 'Yes, it contains the string "a"'
if name.find('war') != -1 :
    print 'Yes, it contains string "war"'
delimiter = '-*-'
mylist = ['brazil','Russia','India','China']
print delimiter.join(mylist)