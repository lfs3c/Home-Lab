# LF1 MCP Server

**Status:** Milestone 1 complete — authenticated Hermes → LF1 MCP communication

## Purpose

The LF1 MCP Server is a security-focused interface that lets Hermes interact with the Home Lab through explicit, controlled MCP tools.

The previous Hermes Control API is frozen and retained only as a reference/fallback. New Home Lab integration work is being developed through MCP.

## Milestone 1

Verified end-to-end:

- official Python MCP SDK (`mcp` 2.2.x)
- local MCP communication over stdio
- Streamable HTTP transport
- persistent systemd service on LF1
- network access restricted by host firewall
- Bearer-token authentication
- anonymous and invalid-token requests rejected with HTTP 401
- valid token successfully initializes an MCP session
- Hermes VM discovers and calls the MCP tools remotely
- `system_health` returns live LF1 health data
- Hermes completed the remote call without using the frozen Control API

## Current tools

| Tool | Access | Purpose |
| --- | --- | --- |
| `ping` | read-only | Confirm that the MCP server is responding |
| `system_health` | read-only | Read hostname, uptime, load averages, memory and root filesystem usage |

## Security model

- least privilege
- read-only first
- explicit MCP tools
- no generic shell or arbitrary command execution
- Bearer authentication for remote MCP access
- credentials stored outside the repository
- host firewall restricts network access
- administrative capabilities require explicit design and review
- Hermes cannot grant itself additional privileges

Runtime credentials, host-specific service configuration, virtual environments and logs are intentionally excluded.
