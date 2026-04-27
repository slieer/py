"""

"""
import logging as log
import json
log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def arr():
    one_dim_arr = ['可以', '负数', '切片', '序列', '位置', '返回']
    print('one_dim_arr:', one_dim_arr)
    
    for element in one_dim_arr:
        print(element)
    
    two_dimensional_arr = []
    two_dimensional_arr.append(['新闻', '贴吧'])
    two_dimensional_arr.append(['知道', '音乐'])
    two_dimensional_arr.append(['图片', '视频'])
    
    print('two_dimensional_arr:',two_dimensional_arr)
    
    for el in two_dimensional_arr:
        print(el)

arr()
 
# 1. iter(obj)
# 要求 obj 实现了 __iter__() 方法（如 list, str, dict）或 __getitem__()（支持索引访问）。
# 自定义可迭代对象需实现 __iter__ 和 __next__（或使用生成器）。
lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1


# 2. next(iterator[, default])
# 从迭代器中获取下一个元素。
it = iter([10, 20])
print(next(it))          # 10
print(next(it))          # 20
print(next(it, "end"))   # "end"

# 3. aiter(obj)（Python 3.10+）
#获取异步迭代器，用于 async for 循环。
# 示例（需在 async 上下文中）


# 5. enumerate(iterable, start=0)
# 为可迭代对象添加索引，返回 (index, value) 元组。


for i, char in enumerate("abc", start=1):
    print(i, char)

# 6. map(func, iterable, ...)
# 将 func 应用于 iterable 的每个元素，返回惰性 map 对象（迭代器）。

nums = [1, 2, 3]
squares = map(lambda x: x**2, nums)
print(list(squares))  # [1, 4, 9]
# 多个 iterable
list(map(lambda x, y: x + y, [1,2], [10,20]))  # [11, 22]

# 7. filter(func, iterable)
# 过滤 iterable 中使 func(item) 为 True 的元素。

evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(evens))  # [2, 4]

# 过滤真值（func=None 等价于 bool）
truthy = filter(None, [0, "", "hello", [], [1]])
print(list(truthy))  # ['hello', [1]]

# 8. zip(*iterables)
# 并行迭代多个可迭代对象，按位置打包成元组。
a = [1, 2, 3]
b = ['x', 'y', 'z']
print(list(zip(a, b)))  # [(1, 'x'), (2, 'y'), (3, 'z')]

# 解包还原（转置）
pairs = [(1, 'a'), (2, 'b')]
nums, letters = zip(*pairs)
print(nums)     # (1, 2)
print(letters)  # ('a', 'b')
# ⚠️ zip 在最短的 iterable 耗尽时停止。用 itertools.zip_longest 可填充。

# 9. sorted(iterable, key=None, reverse=False)
#返回新列表，对 iterable 排序（不修改原对象）。

words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))           # ['apple', 'banana', 'cherry']
print(sorted(words, reverse=True))      # ['cherry', 'banana', 'apple']

# 按字典值排序
students = [{'name': 'Alice', 'score': 90}, {'name': 'Bob', 'score': 85}]
print(sorted(students, key=lambda s: s['score']))
# [{'name': 'Bob', 'score': 85}, {'name': 'Alice', 'score': 90}]
# 🔁 对比：list.sort() 是原地排序，只适用于 list。

# 10. reversed(seq)
# 返回反向迭代器（要求 seq 支持 __reversed__() 或是序列类型如 list/tuple）。

print(list(reversed([1, 2, 3])))  # [3, 2, 1]
print(''.join(reversed("hello"))) # "olleh"
# 11. all(iterable)
# 所有元素为真（或 iterable 为空）→ True

print(all([1, 2, 3]))   # True
print(all([1, 0, 3]))   # False
print(all([]))          # True（空视为真）
# 12. any(iterable)
# 任一元素为真 → True
print(any([0, 0, 1]))   # True
print(any([0, 0, 0]))   # False
print(any([]))          # False
# ✅ 常用于条件检查：if any(x > 10 for x in data): ...

# 13. sum(iterable, start=0)
# 对数字求和（或字符串拼接？❌ 不推荐！）

print(sum([1, 2, 3]))       # 6
print(sum([[1], [2]], []))  # [1, 2]（但性能差，用 itertools.chain 更好）

# ❌ 避免用于字符串拼接（O(n²)）
# 正确方式：''.join(str_list)
# 14. max(iterable) / min(iterable)
# 返回最大/最小值。也支持 key 函数和多个参数。

print(max([1, 5, 3]))                     # 5
print(max("apple", "banana", key=len))    # "banana"
print(min({'a': 10, 'b': 5}.items(), key=lambda x: x[1]))  # ('b', 5)
#💡 也可直接传多个参数：max(1, 2, 3) → 3