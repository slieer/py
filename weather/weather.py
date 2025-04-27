from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

import requests
from mcp.server.fastmcp import FastMCP


# 初始化 MCP 服务器
mcp = FastMCP("WeatherServer")

HEWEATHER_API_KEY = "34e54ce6cef7419a9f1f5f616a"  # ← 填入你的和风天气Key 去https://dev.qweather.com/这里申请

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
