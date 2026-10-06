# Architecture

## Objective

The MCP Server - LF1 provides ChatGPT and other explicitly authorized MCP clients with narrowly defined capabilities for observing and eventually administering the LF1 Home Lab.

The architecture follows a capability-based model rather than exposing generic operating-system access.

## Current Architecture

    Authorized MCP client
          |
          | MCP Streamable HTTP
          | Bearer authentication
          v
    restricted network path
          |
          v
    MCP Server - LF1
          |
          v
    lf1-mcp.service
    User=lf1-mcp
    Group=lf1-mcp
    NoNewPrivileges=yes
          |
          +----------------------+----------------------+
          |                      |                      |
          v                      v                      v
    Linux local sources     containers_list        storage_list
    /proc, filesystem            |                      |
                                 | GET only             | fixed read-only
                                 v                      | lsblk / df
                         localhost-only proxy           v
                                 |                 local block/storage
                                 v                 metadata
                         Docker Socket Proxy
                                 |
                                 v
                         Docker daemon

Exact LAN addresses, ports, and personal development paths are intentionally omitted from public documentation.

## MCP Transport

Transport:

    Streamable HTTP

For production, configure `LF1_MCP_HOST` to the intended restricted interface and set `LF1_MCP_RESOURCE_URL` to the client-facing endpoint. The public source defaults to loopback for local development.

Network access is restricted by the LF1 firewall. Network source address alone is not considered sufficient authentication. Bearer authentication is therefore enforced by the MCP server.

## Development and Runtime Separation

Development occurs in a local LF1 development workspace.

Production runs from:

    dedicated production runtime

Production uses its own Python virtual environment. Development virtual environments, Git metadata, tests, and caches are not required by the runtime service.

## Service Identity

The MCP server runs under the dedicated system account:

    lf1-mcp

The account has no interactive login shell, is not a sudo user, is not a member of the Docker group, and does not inherit the human administrator's supplementary groups.

## Docker Boundary

Direct Docker socket access is intentionally denied to `lf1-mcp`.

The Docker Socket Proxy is the security boundary between the MCP process and the Docker daemon. The proxy listens only on localhost and exposes only the explicitly permitted read-only container-listing path.

Authorized MCP clients do not choose a generic Docker URL, HTTP method, or command.

## Storage Observability

`storage_list` follows the same explicit-capability model.

Flow:

    Authorized MCP clients -> LF1 MCP -> storage_list -> fixed lsblk/df queries -> normalized response

The capability discovers LF1 block devices dynamically rather than maintaining a hardcoded inventory.

The response identifies its source host, keeping the current implementation local while allowing future authorized servers or VMs to use the same normalized model.

Adding another physical disk to LF1 does not require adding that device to MCP source code.

## systemd Service Observability

The `services_list` MCP capability provides read-only visibility into LF1
systemd services.

The capability queries systemd through a narrowly defined implementation and
normalizes the result before returning it through MCP.

Service discovery is dynamic rather than based on a hard-coded inventory.

Authorized MCP clients are not given arbitrary `systemctl` arguments, arbitrary operating-system
commands, or generic shell access.

## LibreNMS Integration

LibreNMS is an authoritative network-observability source for authorized MCP clients.

Current production path:

    Authorized MCP client
        |
        | MCP Streamable HTTP + Bearer authentication
        v
    MCP Server - LF1
        |
        | network_devices_list
        v
    LibreNMS HTTP API
        |
        v
    Network device inventory

The current integration is read-only and exposes a specific normalized MCP
capability rather than a generic LibreNMS API proxy.

The long-term objective is to progressively register and monitor the Home Lab
network in LibreNMS. Future write operations and device enrollment remain
separate security milestones.

## Current Milestone

ChatGPT is the primary MCP client; other explicitly authorized clients remain supported. LibreNMS Read Phase v1 is complete and `network_device_status` is in production according to the project owner. Its implementation is not included in this public source snapshot. `network_device_add` remains DEV-only and is not exposed in production.
