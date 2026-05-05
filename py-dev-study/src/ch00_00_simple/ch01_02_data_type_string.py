# -*- coding: utf-8 -*-
"""
Created on 2012-7-8
@author: me

# vim:set nu et ts=4 sw=4 cino=>4:
"""

import string
import collections


def str_func_test():
    """内置字符串常量"""

    # 26个小写字母
    print(string.ascii_lowercase)
    # 26个大写字母
    print(string.ascii_uppercase)
    # 26个小写字母和26个大写字母
    print(string.ascii_letters)
    # 10个数字字符
    print(string.digits)
    # 16个十六进制数字字符
    print(string.hexdigits)
    # 8个八进制数字字符
    print(string.octdigits)
    # 64个可打印字符
    print(string.printable)
    # 空白字符
    print(string.whitespace)


"""
字符串类型

Python 中，bytes（字节串）和 str（字符串）是两种截然不同的数据类型，它们的核心区别在于存储的内容和设计用途。
简单来说：
str (字符串)：面向人类，用于处理文本。
bytes (字节串)：面向计算机，用于处理二进制数据。
"""


def str_type_test():
    s = "AB"
    print(s[0])  # 输出: 'A' (字符)
    for c in s:
        print(c)  # 输出: 'A', 'B'

    # 字节串 bytes
    b = b"AB"
    print(b[0])  # 输出: 65 (字符 'A' 的 ASCII 码)
    for byte in b:
        print(byte)  # 输出: 65, 66

    text = "你好"
    print(len(text))  # 输出: 2 (2个字符)

    byte_text = text.encode("utf-8")
    print(len(byte_text))  # 输出: 6 (6个字节)


def str_():
    str1 = "\u52c3\u5229\u53bf"
    print(str1)

    s = "中文"  # unicode编码的文字
    print(s.encode("utf-8"))  # 转换成utf-8格式输出

    text = eval("u" + "'\\u56c3\\u67e4'")
    print(text)

    # 判断变量类型
    if type("I am a string") is str:
        print("is string:", True)

    if isinstance("Another string", str):
        print(True)

    # 判断空字符串
    if "" == str():
        print("空字符串")
    str_ = "This is a sample string"
    print("字符串切片操作:%s" % (str_[-1:-2]))
    tokens = str_.split()
    print("tokens count:%s" % (len(tokens)))
    print("列表切片操作1", tokens[-1], tokens[-2])
    print("列表切片操作2", tokens[2:5])

    name = "Swaroop" """This is a string object"""

    if name.startswith("Swa"):
        print('Yes, the string starts with "Swa"')
    if "a" in name:
        print('Yes, it contains the string "a"')
    if name.find("war") != -1:
        print('Yes, it contains string "war"')
    delimiter = "-*-"
    mylist = ["brazil", "Russia", "India", "China"]
    print(delimiter.join(mylist))


"""
字符串转数字
"""


def str_to():
    print(float("30.7894"))
    print(int("7894"))

    my_string = "MY STRING"
    rev_string = my_string[::-1]
    print(rev_string)


if __name__ == "__main__":
    str_()
    str_func_test()
    str_to()
