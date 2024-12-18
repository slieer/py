# -*- coding: utf-8 -*-
'''
先初始化父类，再初始化子类
Created on 2010-7-7
@author: me
'''
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(('(Initialized SchoolMember: %s)' % self.name()))

    def tell(self):
        '''Tell my details.'''
        print(('Name:"%s" Age:"%s"' % (self.name, self.age)))
    def __del__(self):
        print ('object decontruction.....')

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(('(Initialized Teacher: %s)' % self.name))

    def tell(self):
        SchoolMember.tell(self)
        print(('Salary: "%d"' % self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(('(Initialized Student: %s)' % self.name))

    def tell(self):
        SchoolMember.tell(self)
        print(('Marks: "%d"' % self.marks))

if __name__ == '__main__':
    t = Teacher('Mrs. Shrividya', 40, 30000)
    s = Student('Swaroop', 22, 75)
    
    print() # prints a blank line
    
    members = [t, s]
    print ('......initializing object end......')
    for member in members:
        member.tell() # works for both Teachers and Students 