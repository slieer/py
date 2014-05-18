
'''
Created on 2012-10-5

@author: me
'''
from simple.collections.collection_list import StackTest

s = StackTest(['b','bb'])
s.enterStack("a")
s.enterStack('a1' )
s.enterStack('a11')
s.enterStack('a2')

print s.readStactTop()
print s.popStactTopElement()