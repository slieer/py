# -*- coding: utf-8 -*-
'''
Created on 2010-7-7

@author: me
'''
class Person:
    '''Represent a person.'''
    population =  0
    
    def __init__(self,name):
        '''Initializing the person's data.'''
        self.name = name
        print '(Initializing %s)' %self.name
    
        #When this person is created,he/she
        #adds to the population
        Person.population += 1
        
    #就如同__init__方法一样，还有一个特殊的方法__del__，
    #它在对象消逝的时候被调用。对象消逝即对象不再被使用，
    #它所占用的内存将返回给系统作它用。在这个方法里面，我们只是简单地把Person.population减1。
    #当对象不再被使用时，__del__方法运行，但是很难保证这个方法究竟在 什么时候 运行。
    #如果你想要指明它的运行，你就得使用del语句，就如同我们在以前的例子中使用的那样。
    #    
    def __del__(self):
        '''I am dying'''
        print '%s says bye.' % self.name
        
        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.' % self.name

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
swaroop.__del__();
            
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()
            
swaroop.sayHi()
swaroop.howMany()     
    