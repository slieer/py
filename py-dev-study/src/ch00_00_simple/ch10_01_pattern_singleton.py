# Python 的模块在首次被导入时执行，之后再次导入会直接返回缓存的模块对象。
# 因此，模块本身就是天然的单例。这是最简单、最符合 Python 风格的方式。
from ch10_01_config import config

# 无论导入多少次，config 都是同一个对象

ｐrint(config.get("db", "host"))
