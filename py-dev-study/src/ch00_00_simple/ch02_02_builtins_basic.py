'''
Created on 2026年2月14日

@author: zhai
'''

""" """

# 返回对象的 ASCII 表示（非 ASCII 字符转义）
ascii('飞禽走兽')	

# 二进制
bin("10")
# 八进制字符串
oct('15')
# 十六进制
hex("ff"), 
	

# ord(c) 是 Python 的一个内置函数，用于获取单个字符（字符串）对应的 Unicode 码点（整数）。
# 它是 chr() 函数的反向操作：
# 'A' Unicode 码位转字符
chr(65)
# 65 字符转 Unicode 码位
ord('A')

# 布尔类型转换
bool(0)        # False
bool([1,2])    # True
bool("")       # False

# 数值类型转换
int("42")          # 整数 42
float("3.14")      # 浮点数 3.14
complex(2, 3)      # 复数 (2+3j)
# 注意：字符串必须是合法数字格式，否则会抛出 ValueError。

#字符串表示
s = "hello\nworld"
print(str(s))   # hello
                # world
print(repr(s))  # 'hello\nworld'
# 字节序列
bytes("abc", "utf-8")      # b'abc'
bytes([65, 66, 67])        # b'ABC'
bytearray([65, 66])        # bytearray(b'AB')
# 注意：bytes() 和 bytearray() 接受字符串（需指定编码）、整数列表、或可迭代的整数（0–255）。

# 容器类型(列表、 元组、 集合)
list("abc")        # ['a', 'b', 'c']
tuple([1,2])       # (1, 2)
set([1,1,2])       # {1, 2}

frozenset([1,2])   # frozenset({1, 2}), 转为不可变集合

# x 必须是可迭代对象（如字符串、列表、元组、字典等）。
# 传入的是一个 可迭代对象（具体是一个包含元组的列表），每个元素是一个 键值对（长度为 2 的序列）。
dict([('a', 1), ('b', 2)])
# 这里使用的是 关键字参数（keyword arguments）。
# 在 Python 中，dict(key=value, ...) 会自动把关键字 key 作为字符串键，value 作为对应的值。
dict(a=1, b=2)            

list(range(0, 5))           # [0, 1, 2, 3, 4]
# 0 为起始索引，10 为结束索引（不包含），2 为步长
list(range(0, 10, 2))       # [0, 2, 4, 6, 8]

"""
memoryview(obj) 是 Python 中用于创建内存视图（memory view）对象的内置函数。
它的主要作用是在不复制数据的前提下，提供对支持缓冲协议（buffer protocol）的对象的底层内存的直接访问，从而提升性能、节省内存。

适用对象
obj 必须是一个支持缓冲协议的对象，常见的包括：
bytes
bytearray
array.array
NumPy 数组（如 numpy.ndarray）
其他实现了缓冲接口的自定义类型

核心优势:
零拷贝（Zero-copy）对大数据（如图像、音频、大型数组）进行切片或传递时，避免内存复制，极大提升效率。
高效修改 可直接通过视图修改底层数据（如果原对象可变，如 bytearray）。
跨模块兼容 在 C 扩展、NumPy、Pillow 等库中广泛使用，用于高效数据交换。
"""

#类型转换与构造
# 示例1：从 bytearray 创建 memoryview
data = bytearray(b"Hello")
mv = memoryview(data)

# 修改 memoryview 会直接影响原始数据
mv[0] = ord(b'J')
logging.info('%s', data)  # 输出: bytearray(b'Jello')

# 示例2：切片操作（不复制数据！）
part = mv[1:4]  # 仍是 memoryview，共享同一块内存
logging.info(part.tobytes())  # b'ell'


import array
# 创建一个 int16 数组
arr = array.array('h', [1, 2, 3])  # 'h' 表示 short (2字节)
mv = memoryview(arr)

# 将其视为字节序列（每个 int16 拆成两个字节）
byte_mv = mv.cast('B')  # 'B' 表示 unsigned char (1字节)
print(byte_mv.tolist())  # 例如: [1, 0, 2, 0, 3, 0]（小端序）

# 修改字节会影响原数组
byte_mv[0] = 10
print(arr[0])  # 输出: 10

"""
memoryview(obj) 是处理二进制数据和高性能计算时的重要工具，特别适合：
大文件处理
网络协议解析
科学计算（与 NumPy 协同）
避免不必要的内存拷贝
"""

