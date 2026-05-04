from collections import namedtuple
from collections import deque
from collections import Counter

# 定义一个名为 'Point' 的命名元组类，包含字段 'x' 和 'y'
Point = namedtuple("Point", ["x", "y"])

p = Point(1, 2)
print(p.x, p.y)  # 输出: 1 2 (通过属性访问)
print(p[0], p[1])  # 输出: 1 2 (仍然支持索引访问)
# p.x = 3  # 报错: AttributeError，因为不可变

"""
队列 (Queue)
队列是一种先进先出的数据结构，允许在队列的末尾添加元素，并在队列的开头删除元素。
"""
d = deque([1, 2, 3])
d.append(4)  # 右端添加: [1, 2, 3, 4]
d.appendleft(0)  # 左端添加: [0, 1, 2, 3, 4]
d.pop()  # 右端弹出: 4, 剩余 [0, 1, 2, 3]
d.popleft()  # 左端弹出: 0, 剩余 [1, 2, 3]


"""
计数器 (Counter) 是Dict的子类，用于统计元素出现的次数的数据结构。
"""
c = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print(c)  # 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(c["apple"])  # 输出: 3
print(c["grape"])  # 输出: 0 (不会报错)
print(c.most_common(2))  # 输出: [('apple', 3), ('banana', 2)]
