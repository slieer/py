'''
Created on 2012-10-6

@author: me
'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# create a set without duplicates
fruit = set(basket)              
# fast membership testing
print 'orange' in fruit
print 'crabgrass' in fruit

a = set('abracadabra')
b = set('alacazam')
print a
print b
print  a - b
print list(a) + list(b)

print a | b
print a ^ b
print a & b
