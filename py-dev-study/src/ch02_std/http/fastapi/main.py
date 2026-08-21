# FastAPI基于Starlette（ASGI框架）和Pydantic构建，天生支持异步编程。
# 通过ASGI接口替代传统WSGI，可充分利用现代异步IO库（如asyncio）实现并发处理。
# 实测数据显示，FastAPI在处理I/O密集型任务时，吞吐量可达传统同步框架（如Flask）的3-5倍，响应延迟降低60%以上。

# ASGI服务器选择
# Uvicorn：轻量级基准实现，适合开发环境
# Gunicorn + UvicornWorker：生产级部署方案
# Hypercorn：支持HTTP/2的多协议服务器

from fastapi import FastAPI
from pydantic import BaseModel

import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


"""
ASGI (Asynchronous Server Gateway Interface) 和 WSGI (Web Server Gateway Interface) 
是用于连接 Web 服务器和 Python Web 应用程序的两种不同的接口标准。

WSGI：WSGI 是一种 Python Web 应用程序与 Web 服务器之间的标准接口。它定义了 Web 应用程序如何接收请求和发送响应的规范，以及中间件等扩展功能的使用方式。WSGI 接口是同步的，即每个请求都在一个单独的线程中执行，直到完成后才返回响应。WSGI 的典型实现包括 Gunicorn、uWSGI 和 mod_wsgi 等。

ASGI：ASGI 是下一代 Python Web 应用程序与 Web 服务器之间的异步接口标准。它扩展了 WSGI 规范，使得 Python Web 应用程序能够处理异步请求，并支持实时通信和长连接等场景。ASGI 接口可以同时处理多个请求，通过异步事件循环来实现高并发性能。ASGI 的典型实现包括 Daphne、Uvicorn 和 Hypercorn 等。

Uvicorn是一个优秀的ASGI服务器，基于uvloop和httptools构建。
"""
import uvicorn

if __name__ == "__main__":
    # 在这里指定 port 和 host
    # 可以命令行指定 --host 0.0.0.0 --port 8000
    uvicorn.run(app, host="0.0.0.0", port=5000)
    logging.info("Starting FastAPI server...")
