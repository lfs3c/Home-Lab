# LF1 MCP Server

Security-focused MCP server that provides Hermes with controlled access to the LF1 Home Lab through explicit, least-privilege capabilities.

## Current Status

The Docker observability milestone is complete.

Current end-to-end path:

    Hermes VM
        |
        | MCP Streamable HTTP + Bearer authentication
        v
    LF1 MCP Server
    192.168.50.18:8000/mcp
        |
        | systemd: lf1-mcp.service
        | User: lf1-mcp
        | NoNewPrivileges=yes
        |
        +-- ping
        |
        +-- system_health
        |
        +-- containers_list
                |
                | HTTP GET
                v
           127.0.0.1:2375
           Docker Socket Proxy
                |
                v
           Docker daemon

## Current MCP Tools

### ping

Confirms that the LF1 MCP Server is responding.

### system_health

Returns read-only host information from authoritative local Linux sources:

- hostname
- uptime
- load averages
- memory usage
- root filesystem usage

### containers_list

Returns a read-only Docker container inventory containing:

- container name
- image
- state
- status
- total container count
- running count
- stopped count

The MCP process does not have direct access to /var/run/docker.sock.

Docker information is obtained through a restricted socket proxy bound only to 127.0.0.1.

## Security Principles

- least privilege
- read-only first
- explicit MCP capabilities
- no generic shell execution
- no arbitrary command execution
- dedicated MCP service identity
- secrets outside the repository
- network restriction plus application authentication
- restricted intermediary for privileged subsystems
- human authorization for future administrative capabilities

## Runtime

Development source:

    /home/leandro/Desktop/Projects/mcp_server

Production runtime:

    /opt/lf1-mcp

Systemd service:

    lf1-mcp.service

Service identity:

    lf1-mcp

The production service account is not a member of the Docker group.

## Documentation

- docs/architecture.md
- docs/security.md
- docs/testing.md
- docs/changelog.md

## Deployment Assets

The restricted Docker socket proxy configuration is stored under:

    deploy/docker_socket_proxy/
