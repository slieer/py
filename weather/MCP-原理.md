MCP（Model Context Protocol） 由 Anthropic 于 2024 年底开源，其目标是为大模型与外部工具 / 数据源之间建立起一座标准化的桥梁，解决兼容性和互操作性问题。从本质上讲，MCP 就像是 AI 领域的 “USB-C 接口”，它定义了一套统一的通信标准，使得大模型能够通过标准化接口连接任意工具，而无需为每个工具单独开发适配代码。


MCP 的技术架构基于经典的客户端 - 服务器模式，主要由三个关键组件构成：MCP Client、MCP Server 和标准协议层。​

支持的通信协议

|协议类型	|应用场景	|数据格式	|典型实现案例 |
| :-----| ----: | :----: |:----: |
|Stdio	|本地工具调用	|JSON-LD	|Cursor代码生成插件|
|HTTP/2	|远程服务交互	|JSON-RPC 2.0	|Claude企业知识库连接|
|SSE	|实时数据流处理	|Server-Sent Events	|金融行情数据订阅|


- -: 设置内容和标题栏居右对齐。
- :- 设置内容和标题栏居左对齐。
- :-: 设置内容和标题栏居中对齐。

Streamable HTTP 的改进
Streamable HTTP 是 MCP 协议的一次重要升级，通过下面的改进解决了原有 HTTP + SSE 传输方式的多个关键问题：

统一端点：移除了专门建立连接的 /sse 端点，将所有通信整合到统一的端点。
按需流式传输：服务器可以灵活选择返回标准 HTTP 响应或通过 SSE 流式返回。
状态管理：引入 session 机制以支持状态管理和恢复。
Streamable HTTP 相比 HTTP + SSE 具有更好的稳定性，在高并发场景下表现更优。
Streamable HTTP 在性能方面相比 HTTP + SSE 具有明显优势，响应时间更短且更稳定。
Streamable HTTP 客户端实现相比 HTTP + SSE 更简单，代码量更少，维护成本更低。


MCP三个核心组件:
1. Resources 允许服务器向LLM公开数据和内容，作为LLM交互的上下文。
2. Prompts
3. Tools 使服务器能够向客户端公开可执行功能。

[modelcontextprotocol](https://modelcontextprotocol.io/introduction)
[python-sdk](https://github.com/modelcontextprotocol/python-sdk)

