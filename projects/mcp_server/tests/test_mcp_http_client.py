import asyncio
import os

import httpx2
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

MCP_URL = os.environ.get("LF1_MCP_URL", "http://127.0.0.1:8000/mcp")


async def main():
    token = os.environ.get("LF1_MCP_TOKEN")
    if not token:
        raise RuntimeError("LF1_MCP_TOKEN is not set")
    async with httpx2.AsyncClient(headers={"Authorization": f"Bearer {token}"}) as http_client:
        async with streamable_http_client(MCP_URL, http_client=http_client) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                print("===== MCP HTTP TOOLS =====")
                for tool in tools.tools:
                    print(f"- {tool.name}: {tool.description}")
                print((await session.call_tool("ping")).content)
                print((await session.call_tool("system_health")).content)


if __name__ == "__main__":
    asyncio.run(main())
