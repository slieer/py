# -*- coding: utf-8 -*-
"""
Created on 2011-9-28

@author: root
"""

# 数字类型 --- int, float, complex
# 布尔类型 - bool
# 迭代器类型
# 序列类型 --- list, tuple, range
# 文本和二进制序列类型方法摘要
# 文本序列类型 --- str
# 二进制序列类型 --- bytes, bytearray, memoryview
# 集合类型 --- set, frozenset
# 映射类型 --- dict
# 上下文管理器类型
# 类型注解的类型 --- Generic Alias、 Union
# 其他内置类型
# 特殊属性


import types

# 提示不要格式化
# fmt: off
ar = [['abc','xyz'],
      ['m','l','n']
     ]
# fmt: on

print(type(ar) is list)
print(isinstance(ar, list))

print(dir(types))
