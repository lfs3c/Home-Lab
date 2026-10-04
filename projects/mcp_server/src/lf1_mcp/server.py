import argparse

from mcp.server import MCPServer
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl

from lf1_mcp.auth import (
    HermesTokenVerifier,
    REQUIRED_SCOPE,
    RESOURCE_URL,
)
from lf1_mcp.tools.system_health import get_system_health
from lf1_mcp.tools.storage_list import get_storage_list
from lf1_mcp.tools.services_list import get_services_list
from lf1_mcp.tools.containers_list import get_containers_list
from lf1_mcp.tools.network_devices_list import get_network_devices_list


mcp = MCPServer(
    "LF1 MCP Server",
    token_verifier=HermesTokenVerifier(),
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("https://auth.invalid"),
        resource_server_url=AnyHttpUrl(RESOURCE_URL),
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


@mcp.tool()
def containers_list() -> dict:
    """Return a read-only list of Docker containers and their states."""
    return get_containers_list()



@mcp.tool()
def storage_list() -> dict:
    """Return read-only LF1 disk, partition, mount, and usage information."""
    return get_storage_list()


@mcp.tool()
def services_list() -> dict:
    """Return read-only LF1 systemd service information."""
    return get_services_list()


@mcp.tool()
def network_devices_list() -> dict:
    """Return read-only network device information from LibreNMS."""
    import os

    base_url = os.environ.get("LIBRENMS_URL")
    token = os.environ.get("LIBRENMS_TOKEN")

    if not base_url or not token:
        raise RuntimeError(
            "LibreNMS credentials are not configured"
        )

    return get_network_devices_list(
        base_url=base_url,
        token=token,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="LF1 MCP Server"
    )

    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http"],
        default="stdio",
        help="MCP transport to use",
    )

    args = parser.parse_args()

    if args.transport == "streamable-http":
        mcp.run(
            "streamable-http",
            host="192.168.50.18",
            port=8000,
            streamable_http_path="/mcp",
        )
    else:
        mcp.run("stdio")


if __name__ == "__main__":
    main()
