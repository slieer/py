"""
Created on 2012-10-6

@author: me
"""

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
# create a set without duplicates
fruit = set(basket)
# fast membership testing
print("orange" in fruit)
print("crabgrass" in fruit)

a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print(a - b)
print(list(a) + list(b))

print(a | b)
print(a ^ b)
print(a & b)

# 直接定义一个集合
s = {1, 2, 3}
s.add(4)
s.remove(1)

lst = [1, 2, 2, 3, 3, 3]
unique = list(set(lst))  # [1, 2, 3]（顺序不保证）
# 若需保留顺序，用 dict.fromkeys (Python 3.7+ 有序)
unique = list(dict.fromkeys(lst))

# 不可变集合，可哈希，可用作字典键
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([1, 2, 3, 4])

# 交集&, 共同元素
fs1.intersection(fs2)
# 并集|, 所有元素
fs1.union(fs2)
# 差集（s1 - s2）, 在 s1 不在 s2
fs1.difference(fs2)
# 对称差集^,
fs1.symmetric_difference(fs2)
# 子集	<=, s1 ⊆ s2
fs1.issubset(fs2)
# 真子集	<	s1 ⊂ s2

# 超集	>=, s1 ⊇ s2
fs1.issuperset(fs2)
