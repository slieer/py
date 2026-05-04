""" """

import logging as log
import asyncio

log.basicConfig(
    level=log.DEBUG, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
)

"""
协程的核心就是：在单线程内，遇到等待就切换，从而避免 CPU 空转。
核心三要素:
要玩转协程，你必须理解这三个核心概念：
async 和 await：定义和使用协程的语法糖。
协程对象 (Coroutine Object)：调用 async 函数后返回的对象，它不会立即执行。
事件循环 (Event Loop)：协程的“调度中心”，负责管理和调度所有协程的执行。

协程 (Coroutine) 是
程序自身（事件循环）运行，
开销极小（用户态切换），
极高（上万甚至十万级），
高并发 I/O（网络、文件）
（始终单线程）

"""


# 使用 async def 来定义一个协程函数(异步函数)
# # 调用 greet("Alice") 不会立即执行，而是返回一个 协程对象（coroutine object）
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
