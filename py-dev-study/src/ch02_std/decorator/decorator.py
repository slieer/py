import functools
import time

"""
装饰器 (Decorator)
装饰器本质上是闭包的一个经典应用。它是一种设计模式，允许你在不修改原函数代码的前提下，为其动态地添加额外的功能。
基本结构
装饰器是一个接收函数作为参数，并返回一个新函数的高阶函数。
"""


def timer(func):
    @functools.wraps(func)  # 保留原函数的元信息，如函数名、文档字符串等
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"正在执行 {func.__name__} 函数...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行耗时: {end_time - start_time:.4f}秒")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "完成"


print("slow_function 执行结果:%s" % (slow_function()))
