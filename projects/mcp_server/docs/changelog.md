# Changelog

## 2026-09-28 - Docker Observability Milestone

### Added

- dedicated `lf1-mcp` system service account;
- production runtime separation under `/opt/lf1-mcp`;
- `NoNewPrivileges=yes`;
- restricted Docker Socket Proxy;
- localhost-only Docker proxy binding on `127.0.0.1:2375`;
- `containers_list` MCP tool;
- unit test for container normalization and summary;
- Docker proxy boundary validation;
- Hermes end-to-end validation of `containers_list`.

### Security

The MCP service runs under the dedicated `lf1-mcp` account.

The MCP service does not inherit membership in the Docker group.

Direct Docker socket access from the MCP service is denied.

Docker container observation is mediated through a restricted proxy.

Sensitive Docker endpoints and state-changing operations tested during this milestone returned HTTP 403.

### Validated MCP Tools

Current application tools:

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
