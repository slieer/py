# -*- coding: utf-8 -*-
'''
Created on 2010-7-3
@author: me
'''

''''Tuple 是不可变 list 
元组里的元素不能改变，字符串也是一种元组。

这样Python才能区分元组和表达式中一个带圆括号的对象。即如果你想要的是一个包含项目2的元组的时候，
你应该指明singleton = (2 , )。
'''
def tupleTest():
        #一个空的元组由一对空的圆括号组成，如myempty = ()。
        empty = ()
        #含有单个元素的元组。必须在第一个（唯一一个）项目后跟一个逗号，
        singleton = 'hello',    # <-- note trailing comma
        len(empty)
        len(singleton)
        
        
        zoo = ('wolf','elephant','penguin')
        print 'Number of animals in the zoo is', len(zoo)
        
        new_zoo = ('monkey','dolphin',zoo)
        print 'Number of animals in the new zoo is', len(new_zoo)
        print "all animals in new zoo are", new_zoo
        print 'Lash animals brought from old zoo is', new_zoo[2][2]
        
        '''
        print语句可以使用跟着%符号的项目元组的字符串。这些字符串具备定制的功能。
        定制让输出满足某种特定的格式。定制可以是%s表示字符串或%d表示整数。
        元组必须按照相同的顺序来对应这些定制。
        '''
        age = 22
        name = 'Swaroop'
        print '%s is %d years old' % (name, age)
        print 'Why is %s playing with that python?' % name 
        
        
def tupleTest1():
        Bob=('bob',30,'male')
        print 'Representation:',Bob
        
        Jane=('Jane',29,'female')
        print 'Field by index:',Jane[0]
        
        for people in [Bob,Jane]:
            print "%s is %d years old %s" % people    

#对比上面的例子，采用namedTuple   
def namedTupleTest():
        import collections
        Person=collections.namedtuple('Person','name age gender')
        print 'Type of Person:',type(Person)
        
        Bob=Person(name='Bob',age=30,gender='male')
        print 'Representation:',Bob
        
        Jane=Person(name='Jane',age=29,gender='female')
        
        print 'Field by Name:',Jane.name
        
        for people in [Bob,Jane]:
            print "%s is %d years old %s" % people

'''''
默认namedtyuple的时候要注意其中的名称不能使用Python的关键字，如：class def等；而且也不能有重复的元素名称，
将namedtuple的重命名模式打开，这样如果遇到Python关键字或者有重复元素名时，自动进行重命名。
'''
def namedTupleTest1():
        import collections
        with_class=collections.namedtuple('Person','name age class gender',rename=True)
        print with_class._fields
        two_ages=collections.namedtuple('Person','name age gender age',rename=True)
        print two_ages._fields    
            
if __name__ == '__main__' :
        tupleTest()
        tupleTest1()
        namedTupleTest()
