#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Created on 2012-11-30
@author: slieer
"""

"""
“鸭子类型”（Duck Typing）并非指某个具体的类或类型，而是一种编程风格和设计理念。它的核心思想是：“如果它走起来像鸭子，叫起来也像鸭子，那么它就是鸭子。”
这意味着 Python 不关心一个对象的具体类型（它是什么），而只关心它是否具备特定的行为或方法（它能做什么）。

因此，Python 中充满了基于这种理念的“鸭子类型”，它们通常表现为一套约定俗成的协议（Protocol）。
总而言之，鸭子类型是 Python 灵活性和强大能力的基石。它鼓励开发者关注对象的行为而非其继承体系，从而编写出更通用、更解耦、更易于复用的代码。

可迭代对象 (Iterable)
任何实现了 __iter__() 方法或 __getitem__() 方法的对象，都可以被 for 循环遍历。
任何实现了 __getitem__() 方法的对象，不仅可以通过索引访问元素，还可以支持切片操作。


支持 len() 函数的对象
任何实现了 __len__() 方法的对象，都可以被 len() 函数调用。


文件类对象 (File-like Object)
任何实现了 read() 和/或 write() 方法的对象，都可以像文件一样被处理。这在处理网络流、内存数据或进行单元测试时非常有用。


上下文管理器 (Context Manager)
任何实现了 __enter__() 和 __exit__() 方法的对象，都可以用在 with 语句中，用于资源的自动管理（如文件关闭、锁释放）。


容器对象 (Container)
任何实现了 __contains__() 方法的对象，都可以使用 in 操作符来检查成员资格。


可调用对象 (Callable)
任何实现了 __call__() 方法的对象，都可以像函数一样被调用。


可等待对象
任何实现了 __await__() 方法的对象都是可等待的，可以用在 await 表达式中。这是 asyncio 异步编程的基础。协程对象（由 async def 函数创建）就是典型的可等待对象。


支持数学运算的对象
通过实现特殊方法，自定义对象可以支持各种数学运算符，使其行为像数字一样。
__add__: 支持 + 运算符
__sub__: 支持 - 运算符
__mul__: 支持 * 运算符
__truediv__: 支持 / 运算符


//	__floordiv__(self, other)	实现地板除 a // b
%	__mod__(self, other)	实现取模 a % b
**	__pow__(self, other)	实现幂运算 a ** b
+=	__iadd__(self, other)	实现原地加法 a += b


==	__eq__(self, other)	实现等于比较 a == b
!=	__ne__(self, other)	实现不等于比较 a != b
<	__lt__(self, other)	实现小于比较 a < b
<=	__le__(self, other)	实现小于等于比较 a <= b
>	__gt__(self, other)	实现大于比较 a > b
>=	__ge__(self, other)	实现大于等于比较 a >= b



-	__neg__(self)	实现取负 -a
+	__pos__(self)	实现取正 +a
~	__invert__(self)	实现按位取反 ~a
abs()	__abs__(self)	实现内置 abs() 函数


str()	__str__(self)	定义 print() 或 str() 的输出，面向用户
repr()	__repr__(self)	定义 repr() 的输出，面向开发者，用于调试
bool()	__bool__(self)	定义对象的真值，用于 if 条件判断
len()	__len__(self)	定义 len() 函数的返回值
int()	__int__(self)	定义 int() 函数的转换行为


obj[key]	__getitem__(self, key)	实现索引或键访问 obj[key]
obj[key] = val	__setitem__(self, key, value)	实现索引或键赋值
del obj[key]	__delitem__(self, key)	实现删除操作
in	__contains__(self, item)	实现成员检查 item in obj

"""
