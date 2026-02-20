"""

"""
import logging as log
import json
log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

import builtins
# 检查是否在 builtins 中
print('abs' in dir(builtins))      # True
print('sqrt' in dir(builtins))     # False

abs(-5)
abs(3+4j)
# 四舍五入到指定小数位（默认为整数）
# ⚠️ 使用“银行家舍入”（偶数优先）	round(3.1415, 2) → 3.14
round(2.5)
round(3.5)
# 计算 base ** exp，若提供 mod 则返回 (base ** exp) % mod（高效模幂）
pow(2, 10, 1000)
pow(2, 3)

# 返回最小值	
min([1, 2, 3])
min(5, 2, 8)

max([1, 2, 3])
max(5, 2, 8)

sum([1, 2, 3])
sum([[1], [2]], [])

divmod(10, 3)  # → (3, 1)
divmod(7.5, 2) # → (3.0, 1.5)

complex(3, 4) # → (3+4j)
complex('3+4j') # → (3+4j)

int(3.9) # → 3

float('3.14') #→ 3.14
float('inf') #→ inf

# 'as' 用于重命名模块、异常或上下文管理器。
import math as m
print(m.sqrt(16))
