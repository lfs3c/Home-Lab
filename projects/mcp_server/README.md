# LF1 MCP Server

![Status](https://img.shields.io/badge/Status-Storage%20Observability%20Complete-28A745) ![MCP](https://img.shields.io/badge/MCP-Server-6C63FF) ![LF1](https://img.shields.io/badge/Host-LF1-A81D33?logo=debian&logoColor=white) ![Security](https://img.shields.io/badge/Security-Least%20Privilege-28A745)

Security-focused MCP server that provides Hermes with controlled access to the LF1 Home Lab through explicit, least-privilege capabilities.

## Current Status

Storage observability is complete.

Current end-to-end path:

    Hermes VM
        |
        | MCP Streamable HTTP + Bearer authentication
        v
    LF1 MCP Server
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
        |       |
        |       | HTTP GET through localhost-only proxy
        |       v
        |   Docker Socket Proxy
        |       |
        |       v
        |   Docker daemon
        |
        +-- storage_list
                |
                +-- fixed read-only lsblk / df queries

Exact LAN addresses, ports, personal development paths, and credentials are intentionally omitted from public documentation.

## Current MCP Tools

### ping

Confirms that the LF1 MCP Server is responding.

### system_health

Returns read-only host information from authoritative local Linux sources, including hostname, uptime, load averages, memory usage, and root filesystem usage.

### containers_list

Returns a read-only Docker container inventory with container name, image, state, status, and summary counts.

The MCP process does not have direct access to the Docker socket. Docker information is obtained through a restricted localhost-only socket proxy.

### storage_list

Returns normalized read-only storage information:

- physical disk name, model, and size
- partitions and filesystem types
- UUIDs
- mount points
- filesystem size and available space
- usage percentage

New disks attached to LF1 are discovered dynamically and do not require source-code changes. The response model includes host/source information so additional authorized hosts can be integrated later without redesigning the storage schema.


### services_list

Returns read-only systemd service observability including normalized service
information and summary counts.

Service discovery comes from systemd rather than from a hard-coded service
inventory. New services can therefore become observable without creating a
new MCP capability for each service.

The capability does not expose arbitrary `systemctl` execution or generic
shell access.

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

    local LF1 development workspace

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
