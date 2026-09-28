# Changelog

## 2026-09-28 - Storage Observability Milestone

### Added

- read-only `storage_list` MCP capability
- dynamic physical disk discovery
- partition and filesystem metadata
- filesystem usage reporting
- UUID and mount-point visibility
- automatic discovery of future LF1 disks
- unit tests for normalized storage output and future-disk discovery
- fresh-session Hermes end-to-end validation using `mcp__lf1__storage_list`

### Security

- fixed `lsblk` and `df` command boundaries
- no Hermes-controlled executable names or command arguments
- no new sudo, group, or proxy privileges
- production execution under the existing `lf1-mcp` service identity
- no Hermes Control API dependency

Milestone status: complete.

## 2026-09-28 - Docker Observability Milestone

### Added

- dedicated `lf1-mcp` system service account
- production runtime separation under `/opt/lf1-mcp`
- `NoNewPrivileges=yes`
- restricted Docker Socket Proxy
- localhost-only Docker proxy binding
- `containers_list` MCP tool
- unit test for container normalization and summary
- Docker proxy boundary validation
- Hermes end-to-end validation of `containers_list`

### Security

The MCP service runs under the dedicated `lf1-mcp` account and does not inherit membership in the Docker group.

Direct Docker socket access from the MCP service is denied. Docker container observation is mediated through a restricted proxy. Sensitive Docker endpoints and state-changing operations tested during this milestone returned HTTP 403.

### Validated MCP Tools

- `ping`
- `system_health`
- `containers_list`

## 0.1.0 - Milestone 1

- created the LF1 MCP Server using the official Python MCP SDK
- implemented `ping` and read-only `system_health`
- validated stdio and Streamable HTTP transports
- configured persistent LF1 service operation and firewall restriction
- added Bearer-token authentication
- validated rejection of missing and invalid credentials
- completed authenticated Hermes VM -> LF1 MCP -> `system_health` end-to-end test
- froze the previous Hermes Control API as a reference/fallback rather than the active development path
