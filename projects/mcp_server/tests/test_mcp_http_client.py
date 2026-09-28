import asyncio
import os

import httpx2

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


MCP_URL = "http://192.168.50.18:8000/mcp"


async def main():
    token = os.environ.get("LF1_MCP_TOKEN")

    if not token:
        raise RuntimeError("LF1_MCP_TOKEN is not set")

    async with httpx2.AsyncClient(
        headers={
            "Authorization": f"Bearer {token}",
        }
    ) as http_client:
        async with streamable_http_client(
            MCP_URL,
            http_client=http_client,
        ) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("===== MCP HTTP TOOLS =====")
                tools = await session.list_tools()

                for tool in tools.tools:
                    print(f"- {tool.name}: {tool.description}")

                print()
                print("===== CALLING ping VIA AUTHENTICATED HTTP =====")
                ping_result = await session.call_tool("ping")

                for content in ping_result.content:
                    if hasattr(content, "text"):
                        print(content.text)

                print()
                print("===== CALLING system_health VIA AUTHENTICATED HTTP =====")
                health_result = await session.call_tool("system_health")

                for content in health_result.content:
                    if hasattr(content, "text"):
                        print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
