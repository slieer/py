from collections.abc import Awaitable, Callable, Sequence
import asyncio, inspect


# 定义一个简单的异步任务函数
async def async_task(name: str, duration: int) -> str:
    await asyncio.sleep(duration)
    return f"Task {name} completed in {duration} seconds."


# 定义一个同步任务函数(就是一个普通函数)
def sync_task(name: str) -> str:
    return f"Task {name} completed instantly."


# 定义一个任务调度器
class TaskScheduler:
    def __init__(self, tasks: Sequence[Callable[..., Awaitable | str]]):
        self.tasks = tasks

    async def run(self) -> None:
        for i, task in enumerate(self.tasks):
            # asyncio.iscoroutinefunction(task)

            if inspect.iscoroutinefunction(task):  # 检查是否是异步函数
                result = await task(f"Async-{i}", i + 1)
            else:  # 否则是同步函数
                result = task(f"Sync-{i}")
            print(result)


# 创建任务列表，包括异步和同步任务
tasks: Sequence[Callable[..., Awaitable | str]] = [
    async_task,  # 异步任务
    sync_task,  # 同步任务
    async_task,  # 异步任务
]


# 使用调度器执行任务
async def main():
    scheduler = TaskScheduler(tasks)
    await scheduler.run()


# 运行主程序
if __name__ == "__main__":
    asyncio.run(main())
