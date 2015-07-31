#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'dev'
"""
 Python 有两个内建的模块用于处理命令行参数：
一个是 getopt，《Deep in python》一书中也有提到，只能简单处理 命令行参数；
另一个是 optparse，它功能强大，而且易于使用，可以方便地生成标准的、符合Unix/Posix 规范的命令行说明。

getopt

在运行程序时，可能需要根据不同的条件，输入不同的命令行选项来实现不同的功能。
目前有短选项和长选项两种格式。短选项格式为"-"加上单个字母选项；长选项为"--"加上一个单词。长格式是在Linux下引入的。
许多Linux程序都支持这两种格式。在Python中提供了getopt模块很好的实现了对这两种用法的支持，而且使用简单。

选项的写法要求
　　对于短格式，"-"号后面要紧跟一个选项字母。
如果还有此选项的附加参数，可以用空格分开，也可以不分开。长度任意，可以用引号。如以下是正确的：
-o
-oa
-obbbb
-o bbbb
-o "a b"

　　对于长格式，"--"号后面要跟一个单词。
如果还有些选项的附加参数，后面要紧跟"="，再加上参数。"="号前后不能有空格。如以下是正确的：

--help=file1

　　而这些是不正确的：
-- help=file1
--help =file1
--help = file1
--help= file1
"""

import sys
import getopt

def usage():
    print("Usage:%s [-a|-o|-c] [--help|--output] args....", sys.argv[0])

if "__main__" == __name__:
    #lsArgs = [""];

    try:
        opts,args = getopt.getopt(sys.argv[1:], "ao:c", ["help", "output="])

        print("============ opts ==================")
        print(opts)

        print("============ args ==================")
        print(args)

        #check all param
        for opt,arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit(1)
            elif opt in ("-t", "--test"):
                print("for test option")
            else:
                print("%s  ==> %s" %(opt, arg))

    except getopt.GetoptError:
        print("getopt error!")
        usage()
        sys.exit(1)