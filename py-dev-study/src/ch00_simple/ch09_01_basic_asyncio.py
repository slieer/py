"""

"""
import logging as log
import asyncio

log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# 定义异步函数
# 调用 greet("Alice") 不会立即执行，而是返回一个 协程对象（coroutine object）
async def greet(name):
    print(f"Hello, {name}!")
    return f"Hi {name}"

# 'async' 和 'await' 用于定义和使用异步函数（协程）。
# await 只能在 async def 函数内部使用！
async def main():
    result = await greet("Alice")  # 暂停 main()，直到 greet() 完成
    print(result)

# 运行异步程序：启动事件循环
asyncio.run(main())  # 自动创建并管理事件循环

# async with
# async for
# async generator