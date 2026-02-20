'''
Created on 2017年1月23日

@author: Administrator
'''

"""
打印python关键字
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

from keyword import kwlist

logging.info('Python keyword: %s', kwlist)

"""true, false, none test"""
true_flag = True;
if true_flag == True:
    logging.info('value is true')
false_flag = False
if false_flag:
    logging.info('value is false')
def do_nothing():
    pass

result = 'None returned' if do_nothing() is None else 'Something else returned'
logging.info('None test: %s', result)

x,y = (10, 15)
if x == 10 and y == 15:
    logging.info('if test')
elif x == 10 and y != 15:
    logging.info('elif test')  
else:
    logging.info('else test')      

if 'a' in 'apple':
    print("包含 a")

done = False    
if not done:
    print("尚未完成")

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

#'assert' 断言，用于调试。
x = 5
assert x > 0, "x 必须为正数"


#'break' 跳出循环。
for i in range(10):
    if i == 2:
        continue
    logging.info(i)  # 打印 0,1,3,4
    if i == 5:
        break
    logging.info(i)  # 打印 0 到 4

for item in [1, 2, 3]:
    print(item)


#'global' 在函数内声明使用全局变量。
counter = 0
def increment():
    global counter
    counter += 1

# 'yield' 用于生成器函数，返回一个值并暂停函数。
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)  # 3, 2, 1    

import builtins
builtins_ = dir(builtins)
ar = []
for b in builtins_:
    if b.__contains__('Error'):
        continue
    elif b.__contains__('Exception'):
        continue
    elif b.endswith('Warning'):
        continue    
    ar.append(b)    

logging.info('%s', ar)
"""
7个模块相关
'__build_class__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__'

4个特殊名字
欢迎界面里的copyright，credits，help，license

6个内建常数(直、假、无、省略号、调试、无实现)
'True', 'False', 'None', 'Ellipsis', '__debug__', 'NotImplemented'

68个内建函数
https://docs.python.org/3/library/functions.html

61+3个异常
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""
