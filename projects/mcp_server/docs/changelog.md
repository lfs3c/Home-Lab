# Changelog

## 2026-10-06 — Public documentation and configuration update

- Standardized the public name as MCP Server - LF1 and retained README badges.
- Identified ChatGPT as the primary client, with other explicitly authorized clients supported.
- Recorded owner-confirmed completion of LibreNMS Read Phase v1 and production status of `network_device_status`.
- Kept `network_device_add` DEV-only. Neither newer implementation is included in this source snapshot.
- Removed deployment-specific addresses and paths; made MCP endpoint configuration environment-based.
- Preserved historical Hermes test records.


## 2026-10-04 — LibreNMS read-only network observability

- Added `network_devices_list`.
- Added normalized LibreNMS device inventory and status summaries.
- Added the explicit `requests` dependency.
- Kept LibreNMS credentials outside the repository.
- Promoted and validated the capability on LF1 production.
- Validated end-to-end execution from Hermes.
- Development test suite: 9 passed.
- Established the objective of progressively registering and monitoring the
  Home Lab network through LibreNMS.
- LibreNMS write capabilities remain a separate future milestone.


## 2026-09-29 - systemd Service Observability Milestone

### Added

- `services_list` MCP tool
- read-only systemd service discovery
- normalized service information and summary output
- dynamic discovery of newly added systemd services
- filtering of non-service blocks
- focused unit tests for service normalization and discovery
- Hermes end-to-end validation of `services_list`

### Security

- no generic shell capability was introduced
- Hermes cannot supply arbitrary operating-system commands
- Hermes cannot supply arbitrary `systemctl` commands
- the capability remains read-only
- the MCP service continues to run as the dedicated `lf1-mcp` identity

### Validated MCP Tools

- `ping`
- `system_health`
- `containers_list`
- `storage_list`
- `services_list`

Milestone status: complete.


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
- production runtime separation in a dedicated production directory
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
