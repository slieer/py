#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Apr 25, 2014
@author: root

http://hi.baidu.com/s307497146/item/c5074dbd3a6dfe412aebe390
http://blog.csdn.net/lwnylslwnyls/article/details/8199454

For example:
myprog -f thefile.txt -s xyz a1 a2 a3 
●argument: 
使用者在命令後面所輸入的字串。
    以本例來說,"-f", "thefile.txt", "-s", "xyz", "a1", "a2","a3" 都是 argument。
    在 Python 中,可以使用 sys.argv[1:] 來得到命令列傳進來的argument。為什麼是 sys.argv[1:] ,
    而不是 sys.argv呢?因為命令列收到完整的參數還要加上一個命令本身的檔名,以本例來說, sys.argv應該是: 
    ["myprog", "-f", "thefile.txt", "-s", "xyz", "a1", "a2","a3"] 
    

●option: 
一些傳遞給命令的額外 argument,以改變程式的行為。以本例來說, "-f", "-s" 就是option。 
有幾種 option 的寫法,在 Unix 系統上的傳統寫法是 "-" 後跟著一個字母,例如 "-f", "-s";以及 "-f-s", 和 "-fs", 
在 Unix 系統上都可以被接受。 GNU project 使用另一種方式,以 "--" 後面跟著一串由"-" 分開的字串,
例如 "--file-for-log"。Python 的 optparse 套件只接受以上所提的兩種 option格式。 

顧名思義, option 應該是可有可無的,即使命令中沒有任何的option,程式也應該能夠正確地執行。
如果程式需要使用者輸入某些資料才能咦,那麼也應該是使用 positionalargument 才對。 

●option argument: 
緊跟隨在 option 後的 argument,就是 option argument。以本例來說, "thefile.txt","xyz" 都是 option argument。
指定 option argument 有兩種寫法, "-f thefile" 和"-fthefile", optparse 套件都接受。 
option 亦可以沒有 option argument,意即 option 單獨存在。
這樣的 option 通常做為旗標(flag) 用,代表某個功能的開啟或是關閉。 

●positional argument: 
當一個 argument list 被解讀完後,剩下的就是 positional argument 了!
以本例來說, "a1","a2", "a3" 就是 positionalargument。通常被用在"使用者必須輸入"的資訊上。 

●required option: 
 optparse套件不對這種 option 做出任何的限制或是協助。 

test:
./option_parser_test.py -f filename -s xyz a b c
'''
import sys
from optparse import OptionParser

"""
在 usage 中使用 "%prog" 關鍵字, OptionParser 會自動將其代換為程式名,即sys.args[0]: 
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage="%prog [-f] [-q]", version="%prog1.0") 
""" 
MSG_USAGE = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2...]" 
optParser = OptionParser(MSG_USAGE)

#add_option用来加入选项，action是有store，store_true，store_false等，dest是存储的变量，default是缺省值，help是帮助提示
optParser.add_option("-f", "--file", action = "store", type = "string", dest = "fileName")

#若有一個以上的 option,重覆上述的方式加入(注意:以下省略了 action參數): 
optParser.add_option("-s", "--someopt", type = "string", dest = "someopt")

"""
parser.add_option("-v", action="store_true",dest="verbose")
parser.add_option("-q", action="store_false",dest="verbose")

arser.add_option("-v", action="store_true", dest="verbose",default = True) 
parser.add_option("-q", action="store_false",dest="verbose")
"""
optParser.add_option("-v", action="store_true", dest="verbose", default=False, help="make lots of noise [default]") 

#fakeArgs = sys.argv[1:]
#options, args =optParser.parse_args(fakeArgs)
options, args =optParser.parse_args()
print options.fileName 
print options.someopt 
print args 




