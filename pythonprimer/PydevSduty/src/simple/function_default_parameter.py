'''
Created on 2010-6-28

@author: me
'''
def say(message, times = 1):
    print message * times

say('hello')
say('world',5)

'''''
Keyword Arguments test
'''
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)

'''
Important warning: 
The default value is evaluated only once. 
This makes a difference when the default is a mutable object 
such as a list, dictionary, or instances of most classes. For example, 
the following function accumulates the arguments passed to it on subsequent calls:
'''
def f(a, L=[]):
    L.append(a)
    return L

print f(1)
#print f(2)
print f(3)
