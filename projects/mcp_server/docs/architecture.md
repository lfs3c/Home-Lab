# Architecture

## Objective

The LF1 MCP Server provides Hermes with narrowly defined capabilities for observing and eventually administering the LF1 Home Lab.

The architecture follows a capability-based model rather than exposing generic operating-system access.

## Current Architecture

    Hermes VM
          |
          | MCP Streamable HTTP
          | Bearer authentication
          v
    LaptopU NAT / restricted network path
          |
          v
    LF1 MCP Server
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

The service binds specifically to the LF1 LAN interface rather than all interfaces.

Network access is restricted by the LF1 firewall. Because the Hermes VM reaches LF1 through LaptopU NAT, network source address alone is not considered sufficient authentication. Bearer authentication is therefore enforced by the MCP server.

## Development and Runtime Separation

Development occurs in a local LF1 development workspace.

Production runs from:

    /opt/lf1-mcp

Production uses its own Python virtual environment. Development virtual environments, Git metadata, tests, and caches are not required by the runtime service.

## Service Identity

The MCP server runs under the dedicated system account:

    lf1-mcp

The account has no interactive login shell, is not a sudo user, is not a member of the Docker group, and does not inherit the human administrator's supplementary groups.

## Docker Boundary

Direct Docker socket access is intentionally denied to `lf1-mcp`.

The Docker Socket Proxy is the security boundary between the MCP process and the Docker daemon. The proxy listens only on localhost and exposes only the explicitly permitted read-only container-listing path.

Hermes does not choose a generic Docker URL, HTTP method, or command.

## Storage Observability

`storage_list` follows the same explicit-capability model.

Flow:

    Hermes -> LF1 MCP -> storage_list -> fixed lsblk/df queries -> normalized response

The capability discovers LF1 block devices dynamically rather than maintaining a hardcoded inventory.

The response identifies its source host, keeping the current implementation local while allowing future authorized servers or VMs to use the same normalized model.

Adding another physical disk to LF1 does not require adding that device to MCP source code.
