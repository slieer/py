# 技术说明
## uv
[原文链接](https://blog.csdn.net/qq_20389175/article/details/146559746)
- Question: 什么是 uv 呢和 conda 比有什么区别？
- Answer: 一个用 Rust 编写的超快速 (100x) Python 包管理器和环境管理工具，由 Astral 开发。定位为 pip 和 venv 的替代品，专注于速度、简单性和现代 Python 工作流。

## ython web server
### Starlette
是负责web端（请求路由，并发），是一个ASGI（Asynchronous server Gateway Interface,是一个Python的Web服务器和应用程序服务器之间的接口规范。它允许开发者使用异步编程模型来处理HTTP请求和响应，以提高服务器的性能和可扩展性。）

### Django
是最流行的 Python 框架，受到广泛信任。Django REST Framework 框架的作者是 Tom Christie，Tom Christie 也创造了 Starlette和 Uvicorn。 FastAPI 正是建立在 Starlette 和 Uvicorn 的基础之上。

### Flask
一种轻量级的框架，很适合构建 API，它不包括数据库集成，也没有很多的附带的功能，虽然这Django 那里是默认提供的。


# 天气项目API
[天气项目API](https://dev.qweather.com/)
使用微信注册

# step1. 项目环境配置

## 创建项目目录
```shell
#安装 uv (optional)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv init mcp_server_test
cd mcp_server_test
#创建虚拟环境并激活
uv venv
source .venv/bin/activate
#安装依赖包
uv add "mcp[cli]" httpx requests
```

## 创建 weather.py

```python
#初始化 MCP 服务器
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

HEWEATHER_API_KEY = "你的 key"  # ← 填入你的和风天气Key 去https://dev.qweather.com/这里申请

def get_city_id(city_name: str) -> str:
    """根据中文城市名获取和风天气 location ID"""
    url = "https://geoapi.qweather.com/v2/city/lookup"
    params = {
        "location": city_name,
        "key": HEWEATHER_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("code") == "200" and data.get("location"):
        print(data)
        return data["location"][0]["id"]
    else:
        raise ValueError(f"找不到城市: {city_name}，错误信息: {data}")


def get_weather(city_name: str) -> str:
    """根据城市中文名返回当前天气中文描述"""
    try:
        location_id = get_city_id(city_name)
        url = "https://devapi.qweather.com/v7/weather/now"
        params = {
            "location": location_id,
            "key": HEWEATHER_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data.get("code") != "200":
            return f"天气查询失败：{data.get('code')}"
        now = data["now"]
        return (
            f"🌍 城市: {city_name}\n"
            f"🌤 天气: {now['text']}\n"
            f"🌡 温度: {now['temp']}°C\n"
            f"💧 湿度: {now['humidity']}%\n"
            f"🌬 风速: {now['windSpeed']} m/s\n"
        )
    except Exception as e:
        return f"查询出错：{str(e)}"

@mcp.tool('query_weather', '查询城市天气')
def query_weather(city: str) -> str:
    """
        输入指定城市的中文名称，返回当前天气查询结果。
        :param city: 城市名称
        :return: 格式化后的天气信息
        """
    return get_weather(city)


if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

# Step3. 测试 MCP Server
```shell
#运行测试
mcp dev weather.py

Need to install the following packages:
@modelcontextprotocol/inspector@0.10.2
Ok to proceed? (y) y

Starting MCP inspector...
⚙️ Proxy server listening on port 6277
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

# Step4. open mcp inspector in chrome browser
- http://127.0.0.1:6274/#resources
- click connect button.
- 可以测试工具的使用

# 修改MCP Server 做成 SSE 服务
## weather-v1代码
```python
import mcp.types as types
import requests
import uvicorn
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route

# ================================
# 1) 你的和风天气API Key
# ================================
HEWEATHER_API_KEY = ""  # ← 填入你的和风天气Key（例如 "abc123xxxxxx"）


# ================================
# 2) 查询天气核心逻辑
# ================================
def get_city_id(city_name: str) -> str:
    """根据中文城市名获取和风天气 location ID"""
    url = "https://geoapi.qweather.com/v2/city/lookup"
    params = {
        "location": city_name,
        "key": HEWEATHER_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("code") == "200" and data.get("location"):
        # 如果成功找到城市
        return data["location"][0]["id"]
    else:
        raise ValueError(f"找不到城市: {city_name}，错误信息: {data}")


def get_weather(city_name: str) -> str:
    """根据城市中文名返回当前天气（中文描述、温度、湿度、风速）"""
    try:
        location_id = get_city_id(city_name)
        url = "https://devapi.qweather.com/v7/weather/now"
        params = {
            "location": location_id,
            "key": HEWEATHER_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data.get("code") != "200":
            return f"天气查询失败：{data.get('code')}"

        now = data["now"]
        return (
            f"🌍 城市: {city_name}\n"
            f"🌤 天气: {now['text']}\n"
            f"🌡 温度: {now['temp']}°C\n"
            f"💧 湿度: {now['humidity']}%\n"
            f"🌬 风速: {now['windSpeed']} m/s\n"
        )
    except Exception as e:
        return f"查询出错：{str(e)}"


# ================================
# 3) MCP Server 定义
# ================================
app = Server("mcp-weather")

# (A) 工具调用处理器：根据工具名称选择执行逻辑
@app.call_tool()
async def call_tool_handler(
    name: str, arguments: dict
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    MCP 工具调用处理器
    """
    if name == "query_weather":
        if "city" not in arguments:
            raise ValueError("Missing required argument 'city'")
        # 调用上面封装好的 get_weather
        weather_info = get_weather(arguments["city"])
        return [types.TextContent(type="text", text=weather_info)]
    else:
        raise ValueError(f"Unsupported tool name: {name}")


# (B) 工具列表：告知 MCP 端都有哪些可调用的工具
@app.list_tools()
async def list_tools() -> list[types.Tool]:
    """
    定义可用的 MCP 工具列表
    """
    return [
        types.Tool(
            name="query_weather",
            description="查询指定城市天气信息（基于和风天气API）",
            inputSchema={
                "type": "object",
                "required": ["city"],
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "要查询的城市名（中文）"
                    }
                },
            },
        ),
    ]


# ================================
# 4) SSE + Starlette 路由
# ================================
sse = SseServerTransport("/messages/")

async def handle_sse(request):
    """处理 /sse 路由的 SSE 连接，并将其接入 MCP Server。"""
    async with sse.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        # 运行 MCP 应用，处理输入输出
        await app.run(
            streams[0], streams[1], app.create_initialization_options()
        )

starlette_app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=handle_sse),
        Mount("/messages/", app=sse.handle_post_message),
    ],
)

# ================================
# 5) 启动服务器
# ================================
if __name__ == "__main__":
    uvicorn.run(starlette_app, host="127.0.0.1", port=8081)


```
## 运行上面的代码
```shell
uv run weather-v1.py 
```

## 测试
### 使用chrome browser
输入地址: http://localhost:8081/sse
打印并持继续打印日志：
event: endpoint
data: /messages/?session_id=62c484f145494f8e804b5fa74f7e0d63

: ping - 2025-04-24 14:50:07.139826+00:00

: ping - 2025-04-24 14:50:22.141566+00:00

### 使用cherry-studio测试
安装 Cherry-Studio
```shell
./Cherry-Studio-1.2.7-x86_64.AppImage
sudo apt install libfuse2t64 
./Cherry-Studio-1.2.7-x86_64.AppImage  --no-sandbox 
```

1. 在Cherry-Studio中，点击最左下角的“Manage”按钮，然后选择“settings”选项卡, 配置 MCP Server 的地址和端口。
![alt text](./cherry-mcp-conf.png "标注")