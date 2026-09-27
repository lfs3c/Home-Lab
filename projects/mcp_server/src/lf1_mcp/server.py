import argparse
import os

from mcp.server import MCPServer
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl

from lf1_mcp.auth import HermesTokenVerifier, REQUIRED_SCOPE, resource_url
from lf1_mcp.tools.system_health import get_system_health


mcp = MCPServer(
    "LF1 MCP Server",
    token_verifier=HermesTokenVerifier(),
    auth=AuthSettings(
        issuer_url=AnyHttpUrl(os.environ.get("LF1_MCP_ISSUER_URL", "https://auth.invalid")),
        resource_server_url=AnyHttpUrl(resource_url()),
        required_scopes=[REQUIRED_SCOPE],
        validate_token_resource=True,
    ),
)


@mcp.tool()
def ping() -> str:
    """Confirm that the LF1 MCP Server is responding."""
    return "LF1 MCP Server is alive"


@mcp.tool()
def system_health() -> dict:
    """Return read-only health information from the LF1 host."""
    return get_system_health()


def main() -> None:
    parser = argparse.ArgumentParser(description="LF1 MCP Server")
    parser.add_argument("--transport", choices=["stdio", "streamable-http"], default="stdio", help="MCP transport to use")
    args = parser.parse_args()
    if args.transport == "streamable-http":
        mcp.run("streamable-http", host=os.environ.get("LF1_MCP_HOST", "127.0.0.1"), port=int(os.environ.get("LF1_MCP_PORT", "8000")), streamable_http_path="/mcp")
    else:
        mcp.run("stdio")


if __name__ == "__main__":
    main()
