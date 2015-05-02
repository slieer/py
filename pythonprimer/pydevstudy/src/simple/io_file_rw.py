# -*- coding: utf-8 -*-
'''
Created on 2010-7-10
last modified 2012-10-07
@author: me
'''
def fileOp():
        poem = '''\
            programming is fun
            When the works id done
            if you wana make your work also fun:
                use python !
        '''
        
        f = file('poem.txt','w')
        f.write(poem)
        f.close()
        
        f = file('poem.txt')
        while True:
            line = f.readline()
            if len(line) == 0:   ### Zero length indicates EOF
                break;
            print line;
        f.close()

def fileOp1():
        try :
                f = file('xxx.txt')
                print f.readline()
        except IOError as e:
                print 'file not find'
                print e
                
if __name__ == "__main__" :
    #fileOp()
    fileOp1()