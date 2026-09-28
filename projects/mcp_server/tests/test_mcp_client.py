import asyncio
import os
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"

server_params = StdioServerParameters(
    command=str(PROJECT_ROOT / ".venv/bin/python"),
    args=["-m", "lf1_mcp.server"],
    env={
        **os.environ,
        "PYTHONPATH": str(SRC_DIR),
    },
)


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("===== MCP TOOLS =====")
            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            print()
            print("===== CALLING ping =====")
            ping_result = await session.call_tool("ping")

            for content in ping_result.content:
                if hasattr(content, "text"):
                    print(content.text)

            print()
            print("===== CALLING system_health =====")
            health_result = await session.call_tool("system_health")

            for content in health_result.content:
                if hasattr(content, "text"):
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
