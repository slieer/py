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


import uvicorn

if __name__ == "__main__":
    # 在这里指定 port 和 host
    # 可以命令行指定 --host 0.0.0.0 --port 8000
    uvicorn.run(app, host="0.0.0.0", port=5000)
    logging.info("Starting FastAPI server...")
