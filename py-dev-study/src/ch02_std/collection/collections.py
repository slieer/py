from collections import namedtuple
# 定义一个名为 'Point' 的命名元组类，包含字段 'x' 和 'y'
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x, p.y)  # 输出: 1 2 (通过属性访问)
print(p[0], p[1]) # 输出: 1 2 (仍然支持索引访问)
# p.x = 3  # 报错: AttributeError，因为不可变


from collections import deque
d = deque([1, 2, 3])
d.append(4)       # 右端添加: [1, 2, 3, 4]
d.appendleft(0)   # 左端添加: [0, 1, 2, 3, 4]
d.pop()           # 右端弹出: 4, 剩余 [0, 1, 2, 3]
d.popleft()       # 左端弹出: 0, 剩余 [1, 2, 3]


from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

chain = ChainMap(dict1, dict2)
print(chain['a']) # 输出: 1 (来自 dict1)
print(chain['b']) # 输出: 2 (来自 dict1，优先于 dict2)
print(chain['c']) # 输出: 4 (来自 dict2)

chain['d'] = 5    # 默认添加到 dict1
print(dict1)      # dict1 变为 {'a': 1, 'b': 2, 'd': 5}


from collections import Counter
c = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(c)          # 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(c['apple']) # 输出: 3
print(c['grape']) # 输出: 0 (不会报错)
print(c.most_common(2)) # 输出: [('apple', 3), ('banana', 2)]


from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

od.move_to_end('a') # 将 'a' 移到最后
# 现在顺序是 b, c, a


from collections import defaultdict
# 默认值为 int() -> 0
d_int = defaultdict(int)
d_int['count'] += 1 
print(d_int['count']) # 输出: 1 (无需先初始化)

# 默认值为 list() -> []
d_list = defaultdict(list)
d_list['fruits'].append('apple')
print(d_list['fruits']) # 输出: ['apple']


from collections import UserDict

class StrictDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        super().__setitem__(key, value)

sd = StrictDict()
sd['name'] = 'Alice' # 正常
# sd[123] = 'Bob'    # 报错: TypeError