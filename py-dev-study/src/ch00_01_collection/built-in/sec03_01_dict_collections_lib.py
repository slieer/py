from collections import ChainMap
from collections import OrderedDict
from collections import defaultdict
from collections import UserDict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

"""
链映射 (ChainMap)
链映射允许多个字典进行组合，并返回一个视图对象，该视图对象包含所有字典中的键值对。
当访问一个键时，ChainMap 会按照顺序在每个字典中查找，直到找到该键为止。如果在所有字典中都没有找到该键，则会引发 KeyError。
"""
chain = ChainMap(dict1, dict2)
print(chain["a"])  # 输出: 1 (来自 dict1)
print(chain["b"])  # 输出: 2 (来自 dict1，优先于 dict2)
print(chain["c"])  # 输出: 4 (来自 dict2)

chain["d"] = 5  # 默认添加到 dict1
print(dict1)  # dict1 变为 {'a': 1, 'b': 2, 'd': 5}

"""
顺序字典 (OrderedDict)
顺序字典是一种字典变体，它保留了键的插入顺序。
当遍历顺序字典时，键会按照插入顺序返回。
"""
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

od.move_to_end("a")  # 将 'a' 移到最后
# 现在顺序是 b, c, a


# 默认值为 int() -> 0
d_int = defaultdict(int)
d_int["count"] += 1
print(d_int["count"])  # 输出: 1 (无需先初始化)

# 默认值为 list() -> []
d_list = defaultdict(list)
d_list["fruits"].append("apple")
print(d_list["fruits"])  # 输出: ['apple']

"""
字典变体 (UserDict)
字典变体是一种字典变体，它允许自定义字典的初始化行为和键值对的处理方式。
"""


class StrictDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        super().__setitem__(key, value)


sd = StrictDict()
sd["name"] = "Alice"  # 正常
# sd[123] = 'Bob'    # 报错: TypeError
