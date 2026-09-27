import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    server = StdioServerParameters(command=".venv/bin/python", args=["-m", "lf1_mcp.server"], env=env)
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("===== MCP TOOLS =====")
            for tool in tools.tools:
                print(f"- {tool.name}")
            print((await session.call_tool("ping")).content)
            print((await session.call_tool("system_health")).content)


if __name__ == "__main__":
    asyncio.run(main())
