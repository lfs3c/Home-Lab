# Architecture

## Objective

The LF1 MCP Server provides Hermes with narrowly defined capabilities for observing and eventually administering the LF1 Home Lab.

The architecture follows a capability-based model rather than exposing generic operating-system access.

## Current Architecture

    Hermes VM
    192.168.122.x
          |
          | MCP Streamable HTTP
          | Bearer authentication
          |
          v
    LaptopU NAT
    192.168.50.88
          |
          v
    LF1
    192.168.50.18:8000
          |
          v
    lf1-mcp.service
    User=lf1-mcp
    Group=lf1-mcp
    NoNewPrivileges=yes
          |
          +----------------------+
          |                      |
          v                      v
    Linux local sources     containers_list
    /proc, filesystem            |
                                  | GET only
                                  v
                            127.0.0.1:2375
                                  |
                                  v
                         Docker Socket Proxy
                                  |
                                  v
                         /var/run/docker.sock
                                  |
                                  v
                            Docker daemon

## MCP Transport

Transport:

    Streamable HTTP

Endpoint:

    http://192.168.50.18:8000/mcp

The service binds specifically to the LF1 LAN address rather than 0.0.0.0.

Network access is restricted by the LF1 firewall.

Because the Hermes VM reaches LF1 through LaptopU NAT, network source address alone is not considered sufficient authentication.

Bearer authentication is therefore enforced by the MCP server.

## Development and Runtime Separation

Development occurs under:

    /home/leandro/Desktop/Projects/mcp_server

Production runs from:

    /opt/lf1-mcp

Production uses its own Python virtual environment.

Development .venv, Git metadata, tests and caches are not required by the runtime service.

## Service Identity

The MCP server runs under the dedicated system account:

    lf1-mcp

The account:

- has no interactive login shell;
- is not a sudo user;
- is not a member of the Docker group;
- does not inherit Leandro's supplementary groups.

## Docker Boundary

Direct Docker socket access is intentionally denied to lf1-mcp.

The Docker Socket Proxy is the security boundary between the MCP process and the Docker daemon.

The proxy listens only on:

    127.0.0.1:2375

The MCP containers_list implementation uses only:

    GET /containers/json?all=true

Hermes does not choose a generic Docker URL, HTTP method or command.
