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
