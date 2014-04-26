import os as s

def osinfo():
    print s.name
    print s.getcwd()
    
osinfo()

listown = [2,3,4]
listtwo = [2 * i for i in listown if i > 2]

print listtwo

def powersum(power,*args):
    """ Return the sum of each argument raised to specified power."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total
print powersum(2,2,4,6)

#def powersum2(power,**args):

import os
print os.getcwd() # Return the current working directory

"""returns a list of all module functions"""
print dir(os) 
help(os)

import math
print math.cos(math.pi / 4.0)
print math.log(1024, 2)
print math.sin(math.e)