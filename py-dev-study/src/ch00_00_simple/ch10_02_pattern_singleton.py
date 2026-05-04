"""
python 设计模式
https://github.com/faif/python-patterns

"""


class Singleton:
    _instance = None  # 类属性，用于存储唯一实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # 如果实例不存在，则调用父类的 __new__ 创建新实例
            cls._instance = super().__new__(cls)
        # 如果实例已存在，则直接返回
        return cls._instance

    def __init__(self, value):
        # 注意：__init__ 每次实例化时都会被调用
        # 如果需要避免重复初始化，可以添加判断逻辑
        self.value = value


s1 = Singleton(10)
s2 = Singleton(20)
print(s1 is s2)  # True，是同一个实例
print(s1.value)  # 20，因为 __init__ 被调用了两次，value 被覆盖
