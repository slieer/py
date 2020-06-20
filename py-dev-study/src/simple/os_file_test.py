# -*- coding: utf-8 -*-
'''
Created on 2012-11-2

@author: me
'''
import os
def osTest():
    currdir = os.getcwd()      # Return the current working directory
    print(currdir)
        
    os.chdir('/server/accesslogs')   # Change current working directory
    os.system('mkdir today')  # Run the command mkdir in the system shell
        
    dir(os)  #<returns a list of all module functions>
    help(os)
        
    import shutil
    shutil.copyfile('data.db', 'archive.db')
    shutil.move('/build/executables', 'installdir')

def fileTest():
    print(os.getcwd())    #得到当前工作目录
    print(os.listdir('.'))   #得到当前目录下的文件
    print(os.listdir('../'))  #得到上一级目录下的文件
        
#     f = file('./file.txt')
        
    fp = open('test.txt', 'w')    #创建空文件
        #print 'is file ?', os.path.isfile(fp)
    print('is file' , os.path.isfile(""))
    print('is dir ?' ,os.path.isdir(fp.name))
        #os.remove('')
    print(os.path.abspath('' ),' \\', fp.name)
        
if __name__ == "__main__" :
    fileTest()
    osTest()
    
        