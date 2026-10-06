![Status](https://img.shields.io/badge/Status-LibreNMS%20Read%20Phase%20v1%20Complete-28A745) ![MCP](https://img.shields.io/badge/MCP-Server-6C63FF) ![LF1](https://img.shields.io/badge/Host-LF1-A81D33?logo=debian&logoColor=white) ![Security](https://img.shields.io/badge/Security-Least%20Privilege-28A745)

# MCP Server - LF1

Security-focused MCP server that provides ChatGPT and other explicitly authorized MCP clients with controlled access to the LF1 Home Lab through explicit, least-privilege capabilities.

## Current Status

LibreNMS Read Phase v1 is complete. ChatGPT is the primary MCP client; other explicitly authorized MCP clients remain supported.

`network_device_status` is in production, as confirmed by the project owner. `network_device_add` remains DEV-only and is not exposed in production.

This public source snapshot includes `network_devices_list` but does not yet include the implementation or tests of `network_device_status` or `network_device_add`. The production milestone is documented here; this checkout alone does not reproduce that newer deployment.

Current end-to-end path:

    Authorized MCP client
        |
        | MCP Streamable HTTP + Bearer authentication
        v
    MCP Server - LF1
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

Confirms that the MCP Server - LF1 is responding.

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

### network_devices_list

Returns a normalized read-only view of network devices currently known by
LibreNMS, including device identity, operating system, status, disabled/ignored
state, and summary counts.

LibreNMS is queried through its HTTP API using credentials stored outside the
repository. The current integration is read-only.

The long-term objective is to progressively register and monitor the Home Lab
network in LibreNMS so authorized MCP clients can use it as an authoritative network-
observability source. Controlled write capabilities and discovery workflows
are separate future security milestones.

### network_device_status (production milestone)

Provides normalized read-only LibreNMS device health. Its production status is owner-confirmed; its implementation is not included in this public snapshot.

### network_device_add (DEV-only)

A separate development write capability. It has not been promoted to production and is not included in this snapshot.

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

    dedicated production runtime outside the development workspace

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

## Runtime Configuration

Set `LF1_MCP_HOST`, `LF1_MCP_PORT`, and `LF1_MCP_RESOURCE_URL` for the intended deployment. The resource URL must match the client-facing MCP endpoint. Defaults use loopback for local development. Keep `LF1_MCP_TOKEN`, `LIBRENMS_URL`, and `LIBRENMS_TOKEN` outside Git.

The Docker proxy loopback binding and protocol port in the deployment example are required to describe its isolation boundary; they are not LAN access instructions.
